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
A closure is a function with an extended scope. It can access non-global variables that are defined outside 
of its body.