# -*- coding: utf-8 -*-

""" Dictionaries and sets

The main value of the ABCs is documenting and formalizing the minimal interfaces for mappings, and serving as criteria for isinstance tests in code that needs to support mappings in a broad sense


What is hashable?
An object is hashable if it has a hash value which never changes during its lifetime(it needs a __hash__() method), and can be compared to other objects(it needs an __eq__() method). Hashable objects whick compare equal must have the same hash value.

A smart way to handle missing keys:

'my_dict.setdefault(key, []).append(new_value)' is the same as running:
if key not in my_dict:
    my_dict[key] = []
my_dict.append(new_value)

Other ways to handle missing key.
1. Use a defaultdict instead of a plain dict.
2. Subclass dict or any other mapping type and add a __missing__ method.


A basic use case of `set` is removing duplication.
Set elements must be hasable. `frozenset` is hashable, so you can have a frozenset element inside a set. 

Smart use of set operations can reduce both the line count and the run time of python programes by reducing loops and lots of conditional
logic.


 Disassembler for Python bytecode, dis.
"""


# Test if the object is mapping type.
import collections.abc as abc
import collections
import re


my_dict = {}
print(isinstance(my_dict, abc.Mapping))


# Build a dict.
a = dict(one=1, two=2, three=3)
b = {'one':1, 'two':2, 'three':3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three':3, 'one':1, 'two':2})
print(a==b==c==d==e)


# 3_1 dict comprehensions
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Banglades'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan')
]
country_code = {country : code for code, country in DIAL_CODES}
print(country_code)
code_country = {code : country.upper() for code, country in DIAL_CODES if code < 66}
print(code_country)


# 3-2 Handle missing keys in a hard way.
WORD_RE = re.compile('\w+')
index = {}
with open('example1_1.py', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

for word in sorted(index, key=str.upper):
    print(word, index[word])


# 3-4 Handle missing keys in a smart way.
WORD_RE = re.compile('\w+')
index = {}
with open('example1_1.py', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
      for match in WORD_RE.finditer(line):
          word = match.group()
          column_no = match.start() + 1
          location = (line_no, column_no)
          index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])


# 3_5 Handle a missing key using defaultdict
WORD_RE = re.compile('\w+')
# The default_factory of a defaultdict is only invoked to provide default values
# for __getitem__ calls, and not for the other methods.
index = collections.defaultdict(list)
with open('example1_1.py', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])


# 3_6, 3_7 Handle a missing key using __missing__()
class StrkeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

d = StrkeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d['4'])
# print(d[1])
print(d.get('2'))
print(d.get(4))
print(d.get(1, 'N/A'))
print(2 in d)
print(1 in d)

#3-10. Count occurrences needles in a haystack, both of type set.
# {} is faster than set()
haystack = {'a', 'b', 'c', 'd'}
needles = {'a', 'b'}
print(len(needles & haystack))