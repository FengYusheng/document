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


if __name__ == '__main__':
    # target()
    main()