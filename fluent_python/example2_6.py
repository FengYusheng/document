# -*- coding: utf-8 -*-

"""
2_6 uses a genexp with a cartesian product to print out a roster of t-shirts of
two colors in three sizes. In contrast with 2_4, here the 6-items list of t-shirts
is never built in memory: the generator expression feeds the for loop producing one
item at a time. If the two lists used in the cartesian product had a thousand items each,
using a generator expression would save the expense of building a list with a million items
just to feed the for loop.

2_7
Use * to grab excess items.

2_8
Nested tuple.

2_9
namedtuple

2_10
namedtuple's attribtes

It’s easy to see the length of a slice or range when only the stop position is given: range(3) and my_list[:3] both produce three items.
It’s easy to compute the length of a slice or range when start and stop are given: just subtract stop - start.
It’s easy to split a sequence in two parts at any index x, without overlapping: simply get my_list[:x] and my_list[x:].

2_11
slice object

Numpy tutorial: http://scipy.github.io/old-wiki/pages/Tentative_NumPy_Tutorial

2_12
Building lists of lists with a list comprehension.

2_14
A riddle

This is an important Python API convetion: functions or methods that change an object
in-place should return None to make it clear to caller that the object itself was changed,
and no new object was created.


2_17
Manage sorted sequence with bisect.

2_20
Show creating, saving and loading an array of 10 million floating-point numbers.

That is nearly 60 times faster than reading the numbers from a text file, which
also involves parsing each line with the float built-in. Saving with array.tofile is about 7 times
faster than writing one float per line in a text file. In addition, the size of the binary file
with 10 million doubles is 80,000,000 bytes (8 bytes per double, zero overhead), while
the text file has 181,515,739 bytes, for the same data.

Another fast and more flexible way of saving numeric data is the pickle module for
object serialization. Saving an array of floats with pickle.dump is almost as
fast as with array.tofile, but pickle handles almost all built-in types, including
complex numbers, nested collections and even instances of user defined classes automatically —
if they are not too tricky in their implementation.


NumPy inspires array memoryview.
https://stackoverflow.com/questions/4845418/when-should-a-memoryview-be-used/


Removing items from the middle of a deque isn't as fast. It is really optimized
for appending and popping from ends.

The append and popleft operations are atomic, so deque is safe to use as a LIFO-queue
in multi-threaded applications without the need for using locks.
"""
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)



a, *body, c, d =range(5)
print(a, body, c, d)


metro_areas = [
    ('Toko', 'JP', 36.933, (35.689722, 139.69167)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))


from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])


print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ':', value)

invoice = """
    0.....6.................................40........52...55........
    1909  Pimoroni PiBrella                     $17.50    3    $52.50
    1489  6mm Tactile Switch x20                 $4.95    2     $9.90
    1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
    1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
    """
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)
l[3::2] = [11, 22]
print(l)
l[2:5] = [100]
print(l)

board = [['_'] * 3 for i in range(3)]
print(board)

weird_board = [['_'] * 3] * 3
weird_board[1][2] = 0
print(weird_board)

# 2_14
# t = (1, 2, [30, 40])
# t[2] += [50, 60]
# print(t)


# 2_17
import bisect

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}      {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))

bisect_fn = bisect.bisect_left
print('DEMO:', bisect_fn.__name__)
print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
demo(bisect_fn)


# 2_18
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])

# 2_19
import random

SIZE = 7

random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)

# 2_20
from array import array
floats = array('d', (random.random() for i in range(10**7)))
print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
print(floats == floats2)

# 2-21. Changing the value of an array item by poking one of its bytes.
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)

# deque approximent O(1) performance. list O(n).
from collections import deque
dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1)
dq.extend([11, 22, 33])
dq.extendleft([10, 20, 30, 40]) # The positions of these itmes are reversed.
print(dq)
