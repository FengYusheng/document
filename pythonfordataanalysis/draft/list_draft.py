#-*-coding: utf-8-*-

import json
from collections import defaultdict, Counter
from pandas import DataFrame, Series
import numpy
import matplotlib
from matplotlib import pylab, mlab, pyplot
np = numpy
plt = pyplot
from IPython.display import display
from IPython.core.pylabtools import figsize, getfigs
from pylab import *
from numpy import *

def get_counts(sequence):
    counts = {}

    for item in sequence:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

def get_counts2(sequence):
    counts = defaultdict(int)

    for item in sequence:
        counts[item] += 1

    return counts

def top_counts(counts, n = 10):
    tz_count_list = [(count, tz) for tz, count in counts.items()]
    tz_count_list.sort()
    return tz_count_list[-n:]

def top_counts2(counts_dict, n = 10):
    tz_count_list = Counter(counts_dict)
    return tz_count_list.most_common(n)

path = '../pydata/pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
# time_zones = [rec[u'tz'] for rec in records if u'tz' in rec]
# counts = get_counts2(time_zones)
# top_ranking = top_counts2(counts)
# print top_ranking

frame = DataFrame(records)
clean_tz = frame[u'tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
tz_counts[:10].plot(kind='barh', rot=0)
pyplot.show()
