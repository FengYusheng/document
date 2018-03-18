# Chapter 7. Fucntion decorators and closures

Fuction decorators let us **"mark"** fuctions in the source code to enhance their behavior. Mastering it requires understanding **closures**.

**closuers** and reserved keywords *`nonlocal`*

Aside from their application in decorators, **closuers** are also essential for asynchronous programming with callbacks, and for coding in a functional style whenever it make sense.

* How Python evaluates decorator syntax?
* How Python decides whether a varable is local?
* Why closures exist and how they work?
* What problem is solved by `nonlocal?`
* Implementing a well-behaved decorator.
* Intersting decorators in the standard library.
* Implementing a parametrized decoartor.

## When Python executes decorators

Decorators are used in many Python Web frameworks.


## Decorator-enhanced Strategy pattern
This solution has several adantages:
* The *promotion* strategy functions don't have to use special names (like the *_promo* suffix).

* The `@promotion` decorator highlights the purpose of the decorated function, and also makes it
easy to temporarily disable a promotion: just comment out the decorator.

* Promotional discount strategies may be defined in other modules, anywhere in the system, 
as long as the `@promotion` decorator is applied to them.


## Variable scope rules
Python doesn't require you to declare variables, but assumes that a variable assigned in the body 
of a function is local. This is much better than the behavior of Javascript, which doesn't require 
variable declare either, but if you forget to declare that a variable is local(with `var`), you may 
clobber a global vairable without knowing.

`global` make interpreter treat `b` as a global variable in spite of the assignment within the function.


## Closures
A closure is a function with an extended scope. It can access non-global variables that are defined outside of its body.

A closure is function that retains the bindings of the free variables that exist when the function is 
defined, so that they can be used later when the function is invoked and the defining scope is no longer 
available.

**Note:** the only situation in which a function may need to deal with external variables that are non-global is when it is nested in another function.


## The `nonlocal` declaration

Example 7-13. A broken higher-order function to caculate a running average without keeping all history.
Can you see where it breaks?

```

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total / count

    return averager
```

The objects stored in `__clousre__` are read-only, you can't change them. If you rebind them, 
as in `count += 1`, you are implicitly creating a local variable count. It's no longer a free variable.

To work around this rule the `nonlocal` declaration was introduced in Python 3.


## Implementing a  simple decorator
The typical behavior of a decorator is replacing the decorated funciton with a new funciton that accepts 
the same arguments and (usually) returns whatever the decorated function was supposed to return, 
while also doing some extra processing.


## Decorators in the standard library
Python has three built-in functions that are designed to decorate methods: 
* `property`
* `classmethod`
* `staticmethod

Trhe frequently seen decorators in standard library are:
* `functools.wraps`
* `functools.lru_cache`
* `functools.singledispatch`

**LRU** stands for *Least Recently Used*, meaning that the growth of the cache is limited 
by discarding the entries that have not been read for a while.


**generic funciton**
A group of functions to perform the same operation in different ways, depending on the type of the first argument.
This is what is meant by the term single-dispatch. If more arguments were used to select the specific function, we'd 
have multiple-dispatch.

https://docs.python.org/3/glossary.html#term-generic-function

>A funciton composed of multiple functions implementing the same operation for diffrent types. Which implementation 
should be used during a call is determined by the dispatch algorithm.

**singel dispatch**
https://docs.python.org/3/glossary.html#term-single-dispatch

>A form of generic function dispatch where the implementation is chosen based on the type of a single argument.

Python doesn't have method or function overloading.

When possible, reigster the specialized functions to handle ABCs (abstract classes) such as `numbers.Intergral` and 
`abc.MutableSequence` instead of concrete implementation like `int` and `list`. **This allows your code to support a 
greater variety of compatible types.** For example, a Python extension can provide alternatives to the `int` type 
with fixed bit lengths as subclasses of `numbers.Integral.`


## Statcked decorators
```
@d1
@d2
def f():
    pass

f = d1(d2(f))
```

## Parametrized Decorators
Make a decorator factory that takes those arguments and returns a decorator, which is then applied to the function to be 
decorated.


## Chapter summary

Mastering closures and `nonlocal` is valuable not only to build decorators, but also to code 
event-oriented programs for GUIs or asynchronous I/O with callbacks.


## Note
Decorators are best coded as classes implementing `__call__`, and not as functions like the examples 
in this chapter.