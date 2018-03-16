# -*- coding: utf-8 -*-

# Example 7-1. A decorator ususally replaces a function with a
# different one.

def deco(func):
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target()')



# Two crucial fact about decorators:
# 1. They replace the decorated function with a different one.
# 2. They are executed immediately when a module is loaded.

# When does Python executes decorators?
# They run right after the decorated fuction is defined. That is 
# usually at "import time".

# Example 7-2. The main point of this exmaple is to emphasize that funciton decorators are 
# executed as soon as the module is imported (import time), but the decorated functions only run when they are
# explicitly invoked (run time).  
# A real decorator is usually defined in one module and applied to functions in other modules.

registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func



@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


# Compute the mean of an ever-increasing series of values.
# Example 7-8. A class-based implementation.
class Average():
    def __init__(self):
        self.series = []


    def __call__(self, value):
        self.series.append(value)
        total = sum(self.series)
        return total / len(self.series)


# Example 7-9. A functional implementation, using a higher order funciton .
# The binding for `series` is kept in the `__closure__` attribute of the returned 
# function `arg`. Each item in `avg.__closure__` corresponds to a name in `avg.__code__.co_freevars`.
# These items are cells, and they have an attribute cell_contents where the actual value can be found.
def make_averager():
    series = []

    def averager(new_average):
        series.append(new_average)
        total = sum(series)
        return total/len(series)

    return averager


# Example 7-14. Calcualte a running average without keeping all history. Fixed with 
# the use of nonlocal
def make_averager2():
    count = 0
    total = 0

    def averager(new_average):
        nonlocal count, total
        count += 1
        total += new_average
        return total / count

    return averager


# Exapmle 7-15. A simple decorator to output the running time of functions.
import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' %(elapsed, name, arg_str, result))
        return result
    return clocked


# Example 7-16. A simple decorator to output the running time of functions.
@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


import functools

def clock2(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, *kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(', '.join(pairs))
        arg_str = ', '.join(arg_list)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


# Exapmle 7-18. The very costly recusive way to compute the Nth number in the Fibonacci series.
# fibonacci(1) is called 8 times, fibonacci(2) 5 time.


@clock
def fibonacci(n):
    """
                        6

                  /            \\
                 4              5
               /  \\        /       \\
              2     3      3         4 
             / \\  / \\   / \\     /  \\
            0   1 1   2  1   2    2     3
                     / \\   / \\ / \\  / \\
                    0   1  0   1 0  1 1   2
                                        /   \\
                                        0    1

    """
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


# Example 7-19. Faster implementation using caching. This is an example of stacked decorators.
# @lru_cache() is applied on the function returned by @clock.

@functools.lru_cache()
@clock
def fibonacci2(n):
    if n < 2:
        return n
    return fibonacci2(n-2) + fibonacci2(n-1)


# Example 7-21. singledispatch creates a custom htmlize.resgister to bundle servral functions into 
# a generic function.

from collections import abc
import numbers
import html

@functools.singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'





if __name__ == '__main__':
    # target()

    # main()

    # avg = Average() 
    # print(avg(10))
    # print(avg(11))
    # print(avg(12))

    # avg = make_averager()
    # avg = make_averager2()
    # print(avg(10))
    # print(avg(11))
    # print(avg(12))
    
    # print(avg.__code__.co_freevars)
    # print(avg.__closure__)
    # print(avg.__closure__[0].cell_contents)

    # print('*'*40, 'Calling snooze(.123)')
    # snooze(.123)
    # print('*'*40, 'Calling factorial(6)')
    # print('6! = ', factorial(6))

    # print(fibonacci(6))

    print(fibonacci2(6))
    print(fibonacci2.cache_info())