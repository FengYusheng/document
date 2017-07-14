# -*- coding: utf-8: -*-

import sys
import os
import json
import time
from collections import deque, Counter
import pymel.core as pm

def timeIt(func):
    def wrapper(*args, **kwargs):
        start = time.clock()
        func(*args, **kwargs)
        end = time.clock()
        print u'{0} costs {1:.2f}'.format(func.__name__, end-start)
    return wrapper


class TestSuite():
    def __init__(self):
        self.scene = pm.system.sceneName()
        self.scene_folder = self.scene.dirname()
        self.file_type = self.scene.getTypeName()[0]
        self.file_name = self.scene.basename().split('.')[0]
        self.geometries = pm.ls(type='mesh', noIntermediate=False)
        self.datas = {
                'totalVerts' : 0,
                'totalEdges' : 0,
                'totalFaces' : 0,
                'totalTris'  : 0,
                'totalUVs'   : 0,
                'overlappingVertices' : None,
                'geometries' : [
                    {
                        'meshNode'            : obj, # pm.nt.Mesh()
                        'transforms'          : None,
                        'textureFiles'        : None,
                        'shaderName'          : None,
                        'ngons'               : None,
                        'lamina'              : None
                    } for obj in self.geometries
                ],
            }

    def _sceneSaved(self):
        if '' == self.scene_folder:
            return False
        else:
            return True

    def _isEmepty(self):
        if 0 == len(self.geometries):
            return True
        else:
            return False

    def _bfs(self, start_node=None, target_type=pm.nt.File):
        # This search excludes all the unused nodes.
        targets = []
        if start_node is None:
            return targets
        sources = pm.listConnections(start_node, d=False, s=True)
        sources = [s for s in sources if isinstance(s, pm.nt.ShadingDependNode)]
        if 0 == len(sources):
            return targets
        d = deque(sources)
        while len(d) > 0:
            node = d.popleft()
            if isinstance(node, target_type):
                targets.append(node)
            sources = pm.listConnections(node, d=False, s=True)
            for node in sources:
                if isinstance(node, pm.nt.ShadingDependNode):
                    d.append(node)
        return targets

    @timeIt
    def getPolyCounts(self):
        if self._isEmepty():
            return
        for obj in self.datas['geometries']:
            parents = pm.listRelatives(obj['meshNode'], ap=True)
            obj['transforms'] = [{'node' : t} for t in parents if isinstance(t, pm.nt.Transform)] or None
            if obj['transforms'] is not None:
                transform_count = len(obj['transforms'])
                obj['Verts'] = obj['meshNode'].numVertices() * transform_count
                obj['Edges'] = obj['meshNode'].numEdges() * transform_count
                obj['Faces'] = obj['meshNode'].numFaces() * transform_count
                obj['UVs']   = obj['meshNode'].numUVs() * transform_count
                # pymel bug: https://github.com/LumaPictures/pymel/issues/388
                # triangles += mesh.numTriangles()
                obj['Tris']  = int(pm.mel.eval('polyEvaluate -triangle {0}'.format(obj['meshNode']))[0]) * transform_count
                self.datas['totalVerts'] += obj['Verts']
                self.datas['totalEdges'] += obj['Edges']
                self.datas['totalFaces'] += obj['Faces']
                self.datas['totalUVs']   += obj['UVs']
                self.datas['totalTris']  += obj['Tris']

    @timeIt
    def getShaderInfo(self):
        if self._isEmepty():
            return
        for obj in self.datas['geometries']:
            connects = pm.listConnections(obj['meshNode'], type='shadingEngine')
            shaders = self._bfs(connects[0], pm.nt.Lambert) if len(connects) else []
            obj['shaderName'] = shaders[0].name() if len(shaders) else None

    @timeIt
    def getFileNodes(self):
        if self._isEmepty():
            return
        for obj in self.datas['geometries']:
            connects = pm.listConnections(obj['meshNode'], type='shadingEngine')
            nodes = self._bfs(connects[0], pm.nt.File) if len(connects) else []
            obj['textureFiles'] = [n.fileTextureName.get() for n in nodes] if len(nodes) else None

    @timeIt
    def getNGons(self):
        if self._isEmepty():
            return
        for obj in self.datas['geometries']:
            pm.select(obj['meshNode'], replace=True)
            pm.polySelectConstraint(mode=3, type=0x0008, size=3)
            # obj['ngons'] = pm.ls(selection=True) or None
            ngons = pm.ls(selection=True) or []
            obj['ngons'] = [n.name() for n in ngons] if len(ngons) else None
            pm.polySelectConstraint(disable=True)
            pm.select(clear=True)

    @timeIt
    def getOverlappingFaces(self):
        if self._isEmepty():
            return
        for obj in self.datas['geometries']:
            pm.select(obj['meshNode'], replace=True)
            pm.polySelectConstraint(mode=3, type=0x0008, topology=2)
            # obj['lamina'] = pm.ls(selection=True) or None
            laminas = pm.ls(selection=True) or []
            obj['lamina'] = [l.name() for l in laminas] if len(laminas) else None
            pm.polySelectConstraint(disable=True)
            pm.select(clear=True)

    @timeIt
    def getOverlappingVertices(self):
        # delete construct history first
        # TODO: multiprocess, interruptable?
        if self._isEmepty():
            return
        def _roundCoordinates(point):
            coordinates = u'[{0:.2f}, {1:.2f}, {2:.2f}]'\
                            .format(point.x, \
                                    point.y, \
                                    point.z)
            return coordinates.replace(u'-0.00', u'0.00')
        counter = Counter()
        for obj in self.datas['geometries']:
            for vertex in obj['meshNode'].vtx:
                position = _roundCoordinates(vertex.getPosition(space='world'))
                pm.select(vertex, replace=True)
                counter += Counter({position:1})
                if counter[position] > 1:
                    if self.datas['overlappingVertices'] is None:
                        self.datas['overlappingVertices'] = []
                    self.datas['overlappingVertices'].append(repr(vertex))

    @timeIt
    def cleanTransformation(self):
        if self._isEmepty():
            return
        center = pm.dt.Point([0, 0, 0])
        for obj in self.datas['geometries']:
            for t in obj['transforms']:
                t.setPivots(center, worldSpace=True)
                # makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
                pm.makeIdentity(t, \
                                apply=True,      \
                                translate=1,     \
                                rotate=1,        \
                                scale=1,         \
                                normal=0,        \
                                preserveNormals=1)

    @timeIt
    def getTransformInfo(self):
        if self._isEmepty():
            return
        for obj in self.datas['geometries']:
            for t in obj['transforms']:
                pivots = t['node'].getPivots(worldSpace=True)
                t['pivots'] = '{0}'.format(pivots)
                t['tx'] = '{0:.2f}'.format(t['node'].tx.get())
                t['ty'] = '{0:.2f}'.format(t['node'].ty.get())
                t['tz'] = '{0:.2f}'.format(t['node'].tz.get())
                t['rx'] = '{0:.2f}'.format(t['node'].rx.get())
                t['ry'] = '{0:.2f}'.format(t['node'].ry.get())
                t['rz'] = '{0:.2f}'.format(t['node'].rz.get())
                t['sx'] = '{0:.2f}'.format(t['node'].sx.get())
                t['sy'] = '{0:.2f}'.format(t['node'].sy.get())
                t['sz'] = '{0:.2f}'.format(t['node'].sz.get())

    def suite(self):
        self.getPolyCounts()
        self.getTransformInfo()
        self.getShaderInfo()
        self.getFileNodes()
        self.getNGons()
        self.getOverlappingFaces()
        # self.getOverlappingVertices()
        # return self.datas

    def saveReport(self):
        for obj in self.datas['geometries']:
            obj['meshNode'] = repr(obj['meshNode'])
            for t in obj['transforms']:
                t['node'] = repr(t['node'])
        with open('D:\project\MindwalkToolsDevWorkspace\Draft\suite_reports.json', 'w') as f:
            json.dump(self.datas, f, indent=4, encoding='utf-8')

        return self.datas

    def printReport(self):
        for obj in self.datas['geometries']:
            obj['meshNode'] = repr(obj['meshNode'])
            for t in obj['transforms']:
                t['node'] = repr(t['node'])
        print json.dumps(self.datas, indent=4, encoding='utf-8')



if __name__ == '__main__':
    suite = TestSuite()
    suite.suite()
    suite.saveReport()
