# -*- coding: utf-8 -*_

"""
What is a "first-class object"?

A "first-class object" as a program entity that can be:
1. created at runtime;
2. assigned to a variable or element in a data structure;
3. passed as argument to a function;
4. returned as the result of a function.

What is "higher order function"?
A fucntion that takes a function as argument or returns a fuction as result is a higher-order fuction.
e.g: map, sorted.

Functional languages commonly offer the map, filter and reduce higher-order functions. Since the introduction
of list comprehensions and generator expressions, they aren't as important.
In python2 map and filter return lists. In python3 they return generators.

To use a higher-order function sometimes it is convenient to create a small, one-off
function. That's why anonymous functions exist. The simple syntax of Python limits the body of
lambda functions to be pure expressions. In other words, the body of a lambda can't make assignments
or use any other Python statement such as while, try etc.
Outside the limited context of arguments to higher-order functions, anonymous functions are
rarely useful in Python.



Functional Programming HOWTO:
https://docs.python.org/3/howto/functional.html

callable() determines whether an object is callable.
Seven flavors of callable objects:
1. User-defined functions
2. Built-in functions
3. Built-in methods
4. Methonds
5. Classes
6. Class instances
7 generator functions
"""


from functools import reduce
from operator import add
import random


# 5-1. Create and test a function, then read ites __doc__ and check its type.
def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n-1)

print(factorial(42))
print(factorial.__doc__)
print(type(factorial))
print(repr(factorial))

#5-2. Use function through a different name, and pass fuction as argument.
fact = factorial
print(fact)
print(fact(5))
a= map(fact, range(11))
print(a)
print(list(a))

#5-3. Sorting a list of words by length.
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))

#5-4. Sorting a list of words by their reversed spelling.
def reverse(word):
    return word[::-1]

print(reverse('testing'))
print(sorted(fruits, key=reverse))

#5-5. Lists of factorials produced with map and filter compared to alternatives coded as list comprehensions.
print(list(map(fact, range(6))))
print([fact(n) for n in range(6)])
print(list(map(fact, filter(lambda n:n%2, range(6)))))
print([fact(n) for n in range(6) if n%2])

#5-6. Sum of integers up to 99 performed with reduce and sum.
print(reduce(add, range(100)))
print(sum(range(100)))

#5-7. Sorting a list of words by their reversed spelling using lambda.
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=lambda word : word[::-1]))

#5-8 bingocall.py: A BingoCage does one thing: picks items from a shuffled list.
# A class implementing __call__ is an easy way to create function-like objects that have some internal state that must be kept
# across invocations. An example is a decorator.
class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from emtpy BingCage')

    # Shortcut to bingo.pick(): bingo()
    def __call__(self):
        return self.pick()

bingo = BingoCage(range(3))
print(bingo.pick())
print(callable(bingo))
