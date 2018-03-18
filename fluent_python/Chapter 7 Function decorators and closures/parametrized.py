# -*- coding: utf-8 -*-

# Example 7-23. register is our decorator factory.

registry = set()

def register(active=True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)' % (active, func))

        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func
    return decorate


@register(active=False)
def f1():
    print('running f1()')


# register is called as a function to return the actual decorator, decorate.
@register()
def f2():
    print('running f2()')


def f3():
    print("running f3()")


# Example 7-25.
import time

DEFAULT_FMT = '[{elapsed:0.8f}s {name}({args}) -> {result}]'

def clock(fmt=DEFAULT_FMT):
    def decorator(func):
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorator


@clock()
def snooze(seconds):
    time.sleep(seconds)


if __name__ == '__main__':
    # f1()
    # f2()
    # f3()

    for i in range(3):
        snooze(.123)