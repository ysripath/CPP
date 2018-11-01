Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sa17/overview.py ==========
[('/images/NASA-logosmall.gif', 1861),
 ('/images/MOSAIC-logosmall.gif', 1572),
 ('/images/WORLD-logosmall.gif', 1569),
 ('/images/USA-logosmall.gif', 1568),
 ('/images/ksclogo-medium.gif', 1555),
 ('/ksc.html', 1337),
 ('/images/KSC-logosmall.gif', 1083),
 ('/history/apollo/images/apollo-logo1.gif', 543),
 ('/', 534),
 ('/images/launch-logo.gif', 504),
 ('/images/ksclogosmall.gif', 444),
 ('/shuttle/missions/missions.html', 372),
 ('/images/launchmedium.gif', 298),
 ('/shuttle/countdown/count70.gif', 293),
 ('/shuttle/countdown/', 284),
 ('/shuttle/missions/sts-69/mission-sts-69.html', 275),
 ('/icons/menu.xbm', 216),
 ('/icons/blank.xbm', 211),
 ('/shuttle/missions/sts-69/sts-69-patch-small.gif', 194),
 ('/icons/image.xbm', 180)]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a = 'hello'
>>> type(a)
<class 'str'>
>>> b = 10
>>> type(b)
<class 'int'>
>>> b = a
>>> type(b)
<class 'str'>
>>> 
>>> 
>>> a
'hello'
>>> b
'hello'
>>> a = 10
>>> type(a)
<class 'int'>
>>> 
>>> # Variables don't have types.
>>> # The objects have types.
>>> 
>>> x = 10       # Make an int object and let "x" refer to it
>>> x = "hello"  # Make a str object and let "x" refer to the new object
>>> 
>>> 
>>> 
>>> s = 'Three\nblind\nmice'    # 5 + 5 + 4 = 14
>>> len(s)
16
>>> print(s)
Three
blind
mice
>>> "C" == "Python"
False
>>> s = r'Three\nblind\nmice'    # 5 + 5 + 4 = 14
>>> len(s)
18
>>> print(s)
Three\nblind\nmice
>>> 
>>> ord('A')
65
>>> hex(ord('A'))
'0x41'
>>> chr(65)
'A'
>>> chr(0x52)
'R'
>>> chr(0x65)
'e'
>>> chr(0x64)
'd'
>>> # ASCII
>>> # ASC II
>>> [ord(c) for c in s]
[84, 104, 114, 101, 101, 92, 110, 98, 108, 105, 110, 100, 92, 110, 109, 105, 99, 101]
>>> s = 'Three\nblind\nmice'    # 5 + 5 + 4 = 14
>>> [ord(c) for c in s]
[84, 104, 114, 101, 101, 10, 98, 108, 105, 110, 100, 10, 109, 105, 99, 101]
>>> chr(92)
'\\'
>>> chr(110)
'n'
>>> 30 + 40
70
>>> 'hello' + ' world'
'hello world'
>>> [10, 20, 30]
[10, 20, 30]
>>> None
>>> 
>>> 
>>> 
>>> x = 1000
>>> y = 500 + 500
>>> x == y
True
>>> x is y
False
>>> x.__class__                   # dunder class
<class 'int'>
>>> type(x)                       # x.__class__
<class 'int'>
>>> id(x)
4546481264
>>> hex(id(x))
'0x10efdcc70'
>>> hex(id(y))
'0x10efdcdb0'
>>> x = 1000
>>> y = 500 + 500
>>> x is y
False
>>> x == y
True
>>> z = x
>>> x is z
True
>>> hex(id(x))
'0x10efdcdf0'
>>> hex(id(z))
'0x10efdcdf0'
>>> 
Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sa17/overview.py ==========
[('/images/NASA-logosmall.gif', 1861),
 ('/images/MOSAIC-logosmall.gif', 1572),
 ('/images/WORLD-logosmall.gif', 1569),
 ('/images/USA-logosmall.gif', 1568),
 ('/images/ksclogo-medium.gif', 1555),
 ('/ksc.html', 1337),
 ('/images/KSC-logosmall.gif', 1083),
 ('/history/apollo/images/apollo-logo1.gif', 543),
 ('/', 534),
 ('/images/launch-logo.gif', 504),
 ('/images/ksclogosmall.gif', 444),
 ('/shuttle/missions/missions.html', 372),
 ('/images/launchmedium.gif', 298),
 ('/shuttle/countdown/count70.gif', 293),
 ('/shuttle/countdown/', 284),
 ('/shuttle/missions/sts-69/mission-sts-69.html', 275),
 ('/icons/menu.xbm', 216),
 ('/icons/blank.xbm', 211),
 ('/shuttle/missions/sts-69/sts-69-patch-small.gif', 194),
 ('/icons/image.xbm', 180)]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a = 'hello'
>>> type(a)
<class 'str'>
>>> b = 10
>>> type(b)
<class 'int'>
>>> b = a
>>> type(b)
<class 'str'>
>>> 
>>> 
>>> a
'hello'
>>> b
'hello'
>>> a = 10
>>> type(a)
<class 'int'>
>>> 
>>> # Variables don't have types.
>>> # The objects have types.
>>> 
>>> x = 10       # Make an int object and let "x" refer to it
>>> x = "hello"  # Make a str object and let "x" refer to the new object
>>> 
>>> 
>>> 
>>> s = 'Three\nblind\nmice'    # 5 + 5 + 4 = 14
>>> len(s)
16
>>> print(s)
Three
blind
mice
>>> "C" == "Python"
False
>>> s = r'Three\nblind\nmice'    # 5 + 5 + 4 = 14
>>> len(s)
18
>>> print(s)
Three\nblind\nmice
>>> 
>>> ord('A')
65
>>> hex(ord('A'))
'0x41'
>>> chr(65)
'A'
>>> chr(0x52)
'R'
>>> chr(0x65)
'e'
>>> chr(0x64)
'd'
>>> # ASCII
>>> # ASC II
>>> [ord(c) for c in s]
[84, 104, 114, 101, 101, 92, 110, 98, 108, 105, 110, 100, 92, 110, 109, 105, 99, 101]
>>> s = 'Three\nblind\nmice'    # 5 + 5 + 4 = 14
>>> [ord(c) for c in s]
[84, 104, 114, 101, 101, 10, 98, 108, 105, 110, 100, 10, 109, 105, 99, 101]
>>> chr(92)
'\\'
>>> chr(110)
'n'
>>> 30 + 40
70
>>> 'hello' + ' world'
'hello world'
>>> [10, 20, 30]
[10, 20, 30]
>>> None
>>> 
>>> 
>>> 
>>> x = 1000
>>> y = 500 + 500
>>> x == y
True
>>> x is y
False
>>> x.__class__                   # dunder class
<class 'int'>
>>> type(x)                       # x.__class__
<class 'int'>
>>> id(x)
4546481264
>>> hex(id(x))
'0x10efdcc70'
>>> hex(id(y))
'0x10efdcdb0'
>>> x = 1000
>>> y = 500 + 500
>>> x is y
False
>>> x == y
True
>>> z = x
>>> x is z
True
>>> hex(id(x))
'0x10efdcdf0'
>>> hex(id(z))
'0x10efdcdf0'
>>> # None is a singleton
>>> 
>>> s = None
>>> t = None
>>> s == t
True
>>> s is t
True
>>> # Easy to measure features:  [gender, seat]
>>> # Hard to measure features:   C testing
>>> 
>>> 
>>> 
>>> 
>>> d = {'raymond': 'samsung', 'rachel': 'cisco'}
>>> d['rachel']
'cisco'
>>> 
>>> a = 'hello'
>>> type(a)
<class 'str'>
>>> type('hello')
<class 'str'>
>>> 
>>> 
>>> 
>>> 
>>> x = 40                 # 8 bytes in C  28 bytes in Python
>>> 
>>> 
>>> x = 5000
>>> y = x
>>> import sys
>>> sys.getrefcount(x)
3
>>> z = x
>>> sys.getrefcount(x)
4
>>> del y
>>> sys.getrefcount(x)
3
>>> del z
>>> sys.getrefcount(x)
2
>>> del x
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sa17/how_for_loops_work.py =====
0
1
2
3
4
5
6
7
8
9
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sa17/how_for_loops_work.py =====
0
0
1
1
2
2
3
3
4
4
5
5
6
6
7
7
8
8
9
9
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sa17/how_for_loops_work.py =====
0
1
2
3
4
5
6
7
8
9
9
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x = 10
>>> x = 12
>>> x
12
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sa17/how_for_loops_work.py =====
0
1
2
3
4
5
6
7
8
9
5
>>> 
>>> 
>>> 
>>> print('Howdy!')
Howdy!
>>> 38 / 5
7.6
>>> 38 // 5
7
>>> n = 10
>>> for i in range(n):
	pad = ' ' * i
	print(pad, "I'm so hungry. Let's go eat, and resume at 1:15!")

	
 I'm so hungry. Let's go eat, and resume at 1:15!
  I'm so hungry. Let's go eat, and resume at 1:15!
   I'm so hungry. Let's go eat, and resume at 1:15!
    I'm so hungry. Let's go eat, and resume at 1:15!
     I'm so hungry. Let's go eat, and resume at 1:15!
      I'm so hungry. Let's go eat, and resume at 1:15!
       I'm so hungry. Let's go eat, and resume at 1:15!
        I'm so hungry. Let's go eat, and resume at 1:15!
         I'm so hungry. Let's go eat, and resume at 1:15!
          I'm so hungry. Let's go eat, and resume at 1:15!
>>> 

>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
>>> __doc__
' Fast whirlwind tour of most of Python.\n    No time to stop and linger.\n'
>>> n
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
>>> __doc__
' Fast whirlwind tour of most of Python.\n    No time to stop and linger.\n'
>>> # "Repper" is very informative and shows all the special characters but it is not pretty
>>> print(__doc__)
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

>>> # "Stir" is very pretty but has less information
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
>>> __doc__
' Fast whirlwind tour of most of Python.\n    No time to stop and linger.\n'
>>> __name__
'__main__'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

>>> import grand_tour
Hello, my name is grand_tour
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
>>> import grand_tour
Hello, my name is grand_tour
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Oh no! I was imported
>>> # sys.path : list of directories
>>> #    '.'     standard libraries
>>> #    installed libraries   $PYTHONPATH
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'square']
>>> import math
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'math', 'square']
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
121
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
>>> # lambda      ->          make function
>>> lambda x: x**2
<function <lambda> at 0x10dad61e0>
>>> (lambda x: x**2)(15)
225
>>> 1000 + (lambda x: x**2)(15) + 2000
3225
>>> # anonymous functions -- it has no name
>>> # temporary functions -- it doesn't stay around
>>> # in-line functions   -- it can be used in the middle of an expression.
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
>>> 11, 13, 21, 35, 55, 81, 113, 151, 195
(11, 13, 21, 35, 55, 81, 113, 151, 195)

>>> 
>>> 
>>> __name__
'__main__'
>>> __doc__
' Fast whirlwind tour of most of Python.\n    No time to stop and linger.\n'
>>> 
>>> 
>>> type(square)
<class 'function'>
>>> type(type(square))
<class 'type'>
>>> 
>>> 
>>> 
>>> 
>>> square.__name__
'square'
>>> square.__doc__
'Return a value times itself'
>>> square.__module__
'__main__'
>>> square.__class__
<class 'function'>
>>> square.__class__.__name__
'function'
>>> 
>>> 
>>> x = 10
>>> print('The answer is {x} today but was {x**2} yesterday')
The answer is {x} today but was {x**2} yesterday
>>> print(f'The answer is {x} today but was {x**2} yesterday')
The answer is 10 today but was 100 yesterday
>>> 
>>> print(f'The answer')
The answer
>>> print(f"The answer")
The answer
>>> print(F"The answer")
The answer
>>> print(F"yes!")
yes!
>>> 
>>> 
>>> 
>>> func = square
>>> func(5)
25
>>> print(f'The {func.__name__} {func.__class__.__name__} is defined in {func._module}')
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    print(f'The {func.__name__} {func.__class__.__name__} is defined in {func._module}')
AttributeError: 'function' object has no attribute '_module'
>>> print(f'The {func.__name__} {func.__class__.__name__} is defined in {func.__module__}')
The square function is defined in __main__
>>> 
>>> dir(square)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> print(f'The {func.__name__} {func.__class__.__name__} is defined in {func.__module__}')
The square function is defined in __main__
>>> 
>>> def square(x):
    'Return a value times itself'
    return x * x

>>> square.__name__
'square'
>>> square.__class__
<class 'function'>
>>> square.__class__.__name__
'function'
>>> square.__module__
'__main__'
>>> print()

>>> print(func.__doc__)
Return a value times itself
>>> Return a value times itself
SyntaxError: invalid syntax
>>> 
>>> print(f'\t{func.__doc__}')
	Return a value times itself
>>> 
>>> def show_info(func):
	"Display a function's attributes"
	print(f'The {func.__name__} {func.__class__.__name__} is defined in {func.__module__}')
	print()
	print(f'\t{func.__doc__}')
	print()

	
>>> show_info(square)
The square function is defined in __main__

	Return a value times itself

>>> 
def show_info(func):
	"Display a function's attributes"
	print(f'The {func.__name__} {func.__class__.__name__} is defined in {func.__module__}:')
	print()
	print(f'\t{func.__doc__}')
	print()

	
>>> show_info(show_info)
The show_info function is defined in __main__:

	Display a function's attributes

>>> show_info(pow)
The pow builtin_function_or_method is defined in builtins:

	Equivalent to x**y (with two arguments) or x**y % z (with three arguments)

Some types, such as ints, are able to use a more efficient algorithm when
invoked using the three argument form.

>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
>>> 
>>> 
>>> help(square)
Help on function square in module __main__:

square(x)
    Return a value times itself

>>> help(show_info)
Help on function show_info in module __main__:

show_info(func)
    Display a function's attributes

>>> help(pow)
Help on built-in function pow in module builtins:

pow(x, y, z=None, /)
    Equivalent to x**y (with two arguments) or x**y % z (with three arguments)
    
    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.

>>> # Introspection
>>> x = 10
>>> 
>>> x
10
>>> print(f'The answer is {x}')
The answer is 10
>>> 
>>> 
>>> square.__doc__
'Return a value times itself'
>>> 
>>> show_info(square)
The square function is defined in __main__:

	Return a value times itself

>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
>>> 
>>> 
>>> 
>>> import random
>>> help(random)
Help on module random:

NAME
    random - Random variable generators.

MODULE REFERENCE
    https://docs.python.org/3.7/library/random
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
        integers
        --------
               uniform within range
    
        sequences
        ---------
               pick random element
               pick random sample
               pick weighted random sample
               generate random permutation
    
        distributions on the real line:
        ------------------------------
               uniform
               triangular
               normal (Gaussian)
               lognormal
               negative exponential
               gamma
               beta
               pareto
               Weibull
    
        distributions on the circle (angles 0 to 2pi)
        ---------------------------------------------
               circular uniform
               von Mises
    
    General notes on the underlying Mersenne Twister core generator:
    
    * The period is 2**19937-1.
    * It is one of the most extensively tested generators in existence.
    * The random() method is implemented in C, executes in a single Python step,
      and is, therefore, threadsafe.

CLASSES
    _random.Random(builtins.object)
        Random
            SystemRandom
    
    class Random(_random.Random)
     |  Random(x=None)
     |  
     |  Random number generator base class used by bound module functions.
     |  
     |  Used to instantiate instances of Random to get generators that don't
     |  share state.
     |  
     |  Class Random can also be subclassed if you want to use a different basic
     |  generator of your own devising: in that case, override the following
     |  methods:  random(), seed(), getstate(), and setstate().
     |  Optionally, implement a getrandbits() method so that randrange()
     |  can cover arbitrarily large ranges.
     |  
     |  Method resolution order:
     |      Random
     |      _random.Random
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __getstate__(self)
     |      # Issue 17489: Since __reduce__ was defined to fix #759889 this is no
     |      # longer called; we leave it here because it has been here since random was
     |      # rewritten back in 2001 and why risk breaking something.
     |  
     |  __init__(self, x=None)
     |      Initialize an instance.
     |      
     |      Optional argument x controls seeding, as for Random.seed().
     |  
     |  __reduce__(self)
     |      Helper for pickle.
     |  
     |  __setstate__(self, state)
     |  
     |  betavariate(self, alpha, beta)
     |      Beta distribution.
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      Returned values range between 0 and 1.
     |  
     |  choice(self, seq)
     |      Choose a random element from a non-empty sequence.
     |  
     |  choices(self, population, weights=None, *, cum_weights=None, k=1)
     |      Return a k sized list of population elements chosen with replacement.
     |      
     |      If the relative weights or cumulative weights are not specified,
     |      the selections are made with equal probability.
     |  
     |  expovariate(self, lambd)
     |      Exponential distribution.
     |      
     |      lambd is 1.0 divided by the desired mean.  It should be
     |      nonzero.  (The parameter would be called "lambda", but that is
     |      a reserved word in Python.)  Returned values range from 0 to
     |      positive infinity if lambd is positive, and from negative
     |      infinity to 0 if lambd is negative.
     |  
     |  gammavariate(self, alpha, beta)
     |      Gamma distribution.  Not the gamma function!
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      
     |      The probability distribution function is:
     |      
     |                  x ** (alpha - 1) * math.exp(-x / beta)
     |        pdf(x) =  --------------------------------------
     |                    math.gamma(alpha) * beta ** alpha
     |  
     |  gauss(self, mu, sigma)
     |      Gaussian distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.  This is
     |      slightly faster than the normalvariate() function.
     |      
     |      Not thread-safe without a lock around calls.
     |  
     |  getstate(self)
     |      Return internal state; can be passed to setstate() later.
     |  
     |  lognormvariate(self, mu, sigma)
     |      Log normal distribution.
     |      
     |      If you take the natural logarithm of this distribution, you'll get a
     |      normal distribution with mean mu and standard deviation sigma.
     |      mu can have any value, and sigma must be greater than zero.
     |  
     |  normalvariate(self, mu, sigma)
     |      Normal distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.
     |  
     |  paretovariate(self, alpha)
     |      Pareto distribution.  alpha is the shape parameter.
     |  
     |  randint(self, a, b)
     |      Return random integer in range [a, b], including both end points.
     |  
     |  randrange(self, start, stop=None, step=1, _int=<class 'int'>)
     |      Choose a random item from range(start, stop[, step]).
     |      
     |      This fixes the problem with randint() which includes the
     |      endpoint; in Python this is usually not what you want.
     |  
     |  sample(self, population, k)
     |      Chooses k unique random elements from a population sequence or set.
     |      
     |      Returns a new list containing elements from the population while
     |      leaving the original population unchanged.  The resulting list is
     |      in selection order so that all sub-slices will also be valid random
     |      samples.  This allows raffle winners (the sample) to be partitioned
     |      into grand prize and second place winners (the subslices).
     |      
     |      Members of the population need not be hashable or unique.  If the
     |      population contains repeats, then each occurrence is a possible
     |      selection in the sample.
     |      
     |      To choose a sample in a range of integers, use range as an argument.
     |      This is especially fast and space efficient for sampling from a
     |      large population:   sample(range(10000000), 60)
     |  
     |  seed(self, a=None, version=2)
     |      Initialize internal state from hashable object.
     |      
     |      None or no argument seeds from current time or from an operating
     |      system specific randomness source if available.
     |      
     |      If *a* is an int, all bits are used.
     |      
     |      For version 2 (the default), all of the bits are used if *a* is a str,
     |      bytes, or bytearray.  For version 1 (provided for reproducing random
     |      sequences from older versions of Python), the algorithm for str and
     |      bytes generates a narrower range of seeds.
     |  
     |  setstate(self, state)
     |      Restore internal state from object returned by getstate().
     |  
     |  shuffle(self, x, random=None)
     |      Shuffle list x in place, and return None.
     |      
     |      Optional argument random is a 0-argument function returning a
     |      random float in [0.0, 1.0); if it is the default None, the
     |      standard random.random will be used.
     |  
     |  triangular(self, low=0.0, high=1.0, mode=None)
     |      Triangular distribution.
     |      
     |      Continuous distribution bounded by given lower and upper limits,
     |      and having a given mode value in-between.
     |      
     |      http://en.wikipedia.org/wiki/Triangular_distribution
     |  
     |  uniform(self, a, b)
     |      Get a random number in the range [a, b) or [a, b] depending on rounding.
     |  
     |  vonmisesvariate(self, mu, kappa)
     |      Circular data distribution.
     |      
     |      mu is the mean angle, expressed in radians between 0 and 2*pi, and
     |      kappa is the concentration parameter, which must be greater than or
     |      equal to zero.  If kappa is equal to zero, this distribution reduces
     |      to a uniform random angle over the range 0 to 2*pi.
     |  
     |  weibullvariate(self, alpha, beta)
     |      Weibull distribution.
     |      
     |      alpha is the scale parameter and beta is the shape parameter.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  VERSION = 3
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _random.Random:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  getrandbits(...)
     |      getrandbits(k) -> x.  Generates an int with k random bits.
     |  
     |  random(...)
     |      random() -> x in the interval [0, 1).
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from _random.Random:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
    
    class SystemRandom(Random)
     |  SystemRandom(x=None)
     |  
     |  Alternate random number generator using sources provided
     |  by the operating system (such as /dev/urandom on Unix or
     |  CryptGenRandom on Windows).
     |  
     |   Not available on all systems (see os.urandom() for details).
     |  
     |  Method resolution order:
     |      SystemRandom
     |      Random
     |      _random.Random
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  getrandbits(self, k)
     |      getrandbits(k) -> x.  Generates an int with k random bits.
     |  
     |  getstate = _notimplemented(self, *args, **kwds)
     |  
     |  random(self)
     |      Get the next random number in the range [0.0, 1.0).
     |  
     |  seed(self, *args, **kwds)
     |      Stub method.  Not used for a system random number generator.
     |  
     |  setstate = _notimplemented(self, *args, **kwds)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Random:
     |  
     |  __getstate__(self)
     |      # Issue 17489: Since __reduce__ was defined to fix #759889 this is no
     |      # longer called; we leave it here because it has been here since random was
     |      # rewritten back in 2001 and why risk breaking something.
     |  
     |  __init__(self, x=None)
     |      Initialize an instance.
     |      
     |      Optional argument x controls seeding, as for Random.seed().
     |  
     |  __reduce__(self)
     |      Helper for pickle.
     |  
     |  __setstate__(self, state)
     |  
     |  betavariate(self, alpha, beta)
     |      Beta distribution.
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      Returned values range between 0 and 1.
     |  
     |  choice(self, seq)
     |      Choose a random element from a non-empty sequence.
     |  
     |  choices(self, population, weights=None, *, cum_weights=None, k=1)
     |      Return a k sized list of population elements chosen with replacement.
     |      
     |      If the relative weights or cumulative weights are not specified,
     |      the selections are made with equal probability.
     |  
     |  expovariate(self, lambd)
     |      Exponential distribution.
     |      
     |      lambd is 1.0 divided by the desired mean.  It should be
     |      nonzero.  (The parameter would be called "lambda", but that is
     |      a reserved word in Python.)  Returned values range from 0 to
     |      positive infinity if lambd is positive, and from negative
     |      infinity to 0 if lambd is negative.
     |  
     |  gammavariate(self, alpha, beta)
     |      Gamma distribution.  Not the gamma function!
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      
     |      The probability distribution function is:
     |      
     |                  x ** (alpha - 1) * math.exp(-x / beta)
     |        pdf(x) =  --------------------------------------
     |                    math.gamma(alpha) * beta ** alpha
     |  
     |  gauss(self, mu, sigma)
     |      Gaussian distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.  This is
     |      slightly faster than the normalvariate() function.
     |      
     |      Not thread-safe without a lock around calls.
     |  
     |  lognormvariate(self, mu, sigma)
     |      Log normal distribution.
     |      
     |      If you take the natural logarithm of this distribution, you'll get a
     |      normal distribution with mean mu and standard deviation sigma.
     |      mu can have any value, and sigma must be greater than zero.
     |  
     |  normalvariate(self, mu, sigma)
     |      Normal distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.
     |  
     |  paretovariate(self, alpha)
     |      Pareto distribution.  alpha is the shape parameter.
     |  
     |  randint(self, a, b)
     |      Return random integer in range [a, b], including both end points.
     |  
     |  randrange(self, start, stop=None, step=1, _int=<class 'int'>)
     |      Choose a random item from range(start, stop[, step]).
     |      
     |      This fixes the problem with randint() which includes the
     |      endpoint; in Python this is usually not what you want.
     |  
     |  sample(self, population, k)
     |      Chooses k unique random elements from a population sequence or set.
     |      
     |      Returns a new list containing elements from the population while
     |      leaving the original population unchanged.  The resulting list is
     |      in selection order so that all sub-slices will also be valid random
     |      samples.  This allows raffle winners (the sample) to be partitioned
     |      into grand prize and second place winners (the subslices).
     |      
     |      Members of the population need not be hashable or unique.  If the
     |      population contains repeats, then each occurrence is a possible
     |      selection in the sample.
     |      
     |      To choose a sample in a range of integers, use range as an argument.
     |      This is especially fast and space efficient for sampling from a
     |      large population:   sample(range(10000000), 60)
     |  
     |  shuffle(self, x, random=None)
     |      Shuffle list x in place, and return None.
     |      
     |      Optional argument random is a 0-argument function returning a
     |      random float in [0.0, 1.0); if it is the default None, the
     |      standard random.random will be used.
     |  
     |  triangular(self, low=0.0, high=1.0, mode=None)
     |      Triangular distribution.
     |      
     |      Continuous distribution bounded by given lower and upper limits,
     |      and having a given mode value in-between.
     |      
     |      http://en.wikipedia.org/wiki/Triangular_distribution
     |  
     |  uniform(self, a, b)
     |      Get a random number in the range [a, b) or [a, b] depending on rounding.
     |  
     |  vonmisesvariate(self, mu, kappa)
     |      Circular data distribution.
     |      
     |      mu is the mean angle, expressed in radians between 0 and 2*pi, and
     |      kappa is the concentration parameter, which must be greater than or
     |      equal to zero.  If kappa is equal to zero, this distribution reduces
     |      to a uniform random angle over the range 0 to 2*pi.
     |  
     |  weibullvariate(self, alpha, beta)
     |      Weibull distribution.
     |      
     |      alpha is the scale parameter and beta is the shape parameter.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Random:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from Random:
     |  
     |  VERSION = 3
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _random.Random:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from _random.Random:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.

FUNCTIONS
    betavariate(alpha, beta) method of Random instance
        Beta distribution.
        
        Conditions on the parameters are alpha > 0 and beta > 0.
        Returned values range between 0 and 1.
    
    choice(seq) method of Random instance
        Choose a random element from a non-empty sequence.
    
    choices(population, weights=None, *, cum_weights=None, k=1) method of Random instance
        Return a k sized list of population elements chosen with replacement.
        
        If the relative weights or cumulative weights are not specified,
        the selections are made with equal probability.
    
    expovariate(lambd) method of Random instance
        Exponential distribution.
        
        lambd is 1.0 divided by the desired mean.  It should be
        nonzero.  (The parameter would be called "lambda", but that is
        a reserved word in Python.)  Returned values range from 0 to
        positive infinity if lambd is positive, and from negative
        infinity to 0 if lambd is negative.
    
    gammavariate(alpha, beta) method of Random instance
        Gamma distribution.  Not the gamma function!
        
        Conditions on the parameters are alpha > 0 and beta > 0.
        
        The probability distribution function is:
        
                    x ** (alpha - 1) * math.exp(-x / beta)
          pdf(x) =  --------------------------------------
                      math.gamma(alpha) * beta ** alpha
    
    gauss(mu, sigma) method of Random instance
        Gaussian distribution.
        
        mu is the mean, and sigma is the standard deviation.  This is
        slightly faster than the normalvariate() function.
        
        Not thread-safe without a lock around calls.
    
    getrandbits(...) method of Random instance
        getrandbits(k) -> x.  Generates an int with k random bits.
    
    getstate() method of Random instance
        Return internal state; can be passed to setstate() later.
    
    lognormvariate(mu, sigma) method of Random instance
        Log normal distribution.
        
        If you take the natural logarithm of this distribution, you'll get a
        normal distribution with mean mu and standard deviation sigma.
        mu can have any value, and sigma must be greater than zero.
    
    normalvariate(mu, sigma) method of Random instance
        Normal distribution.
        
        mu is the mean, and sigma is the standard deviation.
    
    paretovariate(alpha) method of Random instance
        Pareto distribution.  alpha is the shape parameter.
    
    randint(a, b) method of Random instance
        Return random integer in range [a, b], including both end points.
    
    random(...) method of Random instance
        random() -> x in the interval [0, 1).
    
    randrange(start, stop=None, step=1, _int=<class 'int'>) method of Random instance
        Choose a random item from range(start, stop[, step]).
        
        This fixes the problem with randint() which includes the
        endpoint; in Python this is usually not what you want.
    
    sample(population, k) method of Random instance
        Chooses k unique random elements from a population sequence or set.
        
        Returns a new list containing elements from the population while
        leaving the original population unchanged.  The resulting list is
        in selection order so that all sub-slices will also be valid random
        samples.  This allows raffle winners (the sample) to be partitioned
        into grand prize and second place winners (the subslices).
        
        Members of the population need not be hashable or unique.  If the
        population contains repeats, then each occurrence is a possible
        selection in the sample.
        
        To choose a sample in a range of integers, use range as an argument.
        This is especially fast and space efficient for sampling from a
        large population:   sample(range(10000000), 60)
    
    seed(a=None, version=2) method of Random instance
        Initialize internal state from hashable object.
        
        None or no argument seeds from current time or from an operating
        system specific randomness source if available.
        
        If *a* is an int, all bits are used.
        
        For version 2 (the default), all of the bits are used if *a* is a str,
        bytes, or bytearray.  For version 1 (provided for reproducing random
        sequences from older versions of Python), the algorithm for str and
        bytes generates a narrower range of seeds.
    
    setstate(state) method of Random instance
        Restore internal state from object returned by getstate().
    
    shuffle(x, random=None) method of Random instance
        Shuffle list x in place, and return None.
        
        Optional argument random is a 0-argument function returning a
        random float in [0.0, 1.0); if it is the default None, the
        standard random.random will be used.
    
    triangular(low=0.0, high=1.0, mode=None) method of Random instance
        Triangular distribution.
        
        Continuous distribution bounded by given lower and upper limits,
        and having a given mode value in-between.
        
        http://en.wikipedia.org/wiki/Triangular_distribution
    
    uniform(a, b) method of Random instance
        Get a random number in the range [a, b) or [a, b] depending on rounding.
    
    vonmisesvariate(mu, kappa) method of Random instance
        Circular data distribution.
        
        mu is the mean angle, expressed in radians between 0 and 2*pi, and
        kappa is the concentration parameter, which must be greater than or
        equal to zero.  If kappa is equal to zero, this distribution reduces
        to a uniform random angle over the range 0 to 2*pi.
    
    weibullvariate(alpha, beta) method of Random instance
        Weibull distribution.
        
        alpha is the scale parameter and beta is the shape parameter.

DATA
    __all__ = ['Random', 'seed', 'random', 'uniform', 'randint', 'choice',...

FILE
    /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/random.py


>>> random.__name__
	       
'random'
>>> random.__class__.__name__
	       
'module'
>>> random.__doc__
	       
'Random variable generators.\n\n    integers\n    --------\n           uniform within range\n\n    sequences\n    ---------\n           pick random element\n           pick random sample\n           pick weighted random sample\n           generate random permutation\n\n    distributions on the real line:\n    ------------------------------\n           uniform\n           triangular\n           normal (Gaussian)\n           lognormal\n           negative exponential\n           gamma\n           beta\n           pareto\n           Weibull\n\n    distributions on the circle (angles 0 to 2pi)\n    ---------------------------------------------\n           circular uniform\n           von Mises\n\nGeneral notes on the underlying Mersenne Twister core generator:\n\n* The period is 2**19937-1.\n* It is one of the most extensively tested generators in existence.\n* The random() method is implemented in C, executes in a single Python step,\n  and is, therefore, threadsafe.\n\n'
>>> # bit.ly/python-sa17
	       
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(list)
	       
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Stable sort *IN PLACE*.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> 
	       
>>> 
	       
>>> 
	       
>>> 
	       
>>> help(list.sort)
	       
Help on method_descriptor:

sort(self, /, *, key=None, reverse=False)
    Stable sort *IN PLACE*.

>>> help(list.append)
	       
Help on method_descriptor:

append(self, object, /)
    Append object to the end of the list.

>>> 
	       
>>> 30 + 40
	       
70
>>> 75 - 50
	       
25
>>> _ * 5
	       
125
>>> _ * 4
	       
500
>>> 
	       
>>> # Mac:  Cntl-Prev    Cntl-Next
	       
>>> # Windows:  Alt-Prev  Alt-Next
	       
>>> 30 + 41
	       
71
>>> 75 - 49
	       
26
>>> 
	       
>>> 
	       
>>> 1
	       
1
>>> 2
	       
2
>>> 3
	       
3
>>> 4
	       
4
>>> 5
	       
5
>>> 
	       
>>> 
	       
>>> 30 + 42
	       
72
>>> 
Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sa17/grand_tour.py", line 46, in <module>
    print(len(list))
TypeError: object of type 'type' has no len()
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
>>> 
>>> list(map(type, names))
[<class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>]
>>> 
>>> 
>>> 
>>> type(len)
<class 'builtin_function_or_method'>
>>> #      written in C
>>> len.__module__
'builtins'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
>>> 
>>> 
>>> # Type 2000 lines of Python
>>> names = ['Cisco', 'Samsung', 'Qualcomm', 'Apple']
>>> # Flag to switch to one based indexing
>>> 
>>> i = 2
>>> s[ i ]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s[ i ]
NameError: name 's' is not defined
>>> names[ i ]
'Qualcomm'
>>> names[ i -1]
'Samsung'
>>> 
>>> i = 3
>>> names[ i -1]
'Qualcomm'
>>> i = 4
>>> names[ i -1]
'Apple'
>>> i = 1
>>> names[ i -1]
'Cisco'
>>> 
>>> 
>>> names[ i - 1 ]
'Cisco'
>>> 
>>> 
>>> 
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sa17/grand_tour.py", line 51, in <module>
    print(names[50])
IndexError: list index out of range
>>> 
>>> # FIFO
>>> 
>>> # longjmp()   error handler
>>> 
>>> 
>>> # Exceptions  and  languages I dislike
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sa17/overview.py ==========
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sa17/overview.py", line 8, in <module>
    visited = collections.kounter()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/collections/__init__.py", line 55, in __getattr__
    raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
AttributeError: module 'collections' has no attribute 'kounter'
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sa17/overview.py ==========
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sa17/overview.py", line 8, in <module>
    visited = collections.Counter('xyz', 'qpd')
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/collections/__init__.py", line 564, in __init__
    raise TypeError('expected at most 1 arguments, got %d' % len(args))
TypeError: expected at most 1 arguments, got 2
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sa17/overview.py ==========
[('/images/NASA-logosmall.gif', 1861),
 ('/images/MOSAIC-logosmall.gif', 1572),
 ('/images/WORLD-logosmall.gif', 1569),
 ('/images/USA-logosmall.gif', 1568),
 ('/images/ksclogo-medium.gif', 1555),
 ('/ksc.html', 1337),
 ('/images/KSC-logosmall.gif', 1083),
 ('/history/apollo/images/apollo-logo1.gif', 543),
 ('/', 534),
 ('/images/launch-logo.gif', 504),
 ('/images/ksclogosmall.gif', 444),
 ('/shuttle/missions/missions.html', 372),
 ('/images/launchmedium.gif', 298),
 ('/shuttle/countdown/count70.gif', 293),
 ('/shuttle/countdown/', 284),
 ('/shuttle/missions/sts-69/mission-sts-69.html', 275),
 ('/icons/menu.xbm', 216),
 ('/icons/blank.xbm', 211),
 ('/shuttle/missions/sts-69/sts-69-patch-small.gif', 194),
 ('/icons/image.xbm', 180)]
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sa17/overview.py ==========
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sa17/overview.py", line 9, in <module>
    for filename in glb.glob('notes/*.log'):
NameError: name 'glb' is not defined
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sa17/overview.py ==========
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sa17/overview.py", line 10, in <module>
    with open(filename + 'x') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'notes/nasa_19950801.logx'
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sa17/overview.py ==========
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sa17/overview.py", line 11, in <module>
    for line in None:
TypeError: 'NoneType' object is not iterable
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sa17/overview.py ==========
[('/images/NASA-logosmall.gif', 1861),
 ('/images/MOSAIC-logosmall.gif', 1572),
 ('/images/WORLD-logosmall.gif', 1569),
 ('/images/USA-logosmall.gif', 1568),
 ('/images/ksclogo-medium.gif', 1555),
 ('/ksc.html', 1337),
 ('/images/KSC-logosmall.gif', 1083),
 ('/history/apollo/images/apollo-logo1.gif', 543),
 ('/', 534),
 ('/images/launch-logo.gif', 504),
 ('/images/ksclogosmall.gif', 444),
 ('/shuttle/missions/missions.html', 372),
 ('/images/launchmedium.gif', 298),
 ('/shuttle/countdown/count70.gif', 293),
 ('/shuttle/countdown/', 284),
 ('/shuttle/missions/sts-69/mission-sts-69.html', 275),
 ('/icons/menu.xbm', 216),
 ('/icons/blank.xbm', 211),
 ('/shuttle/missions/sts-69/sts-69-patch-small.gif', 194),
 ('/icons/image.xbm', 180)]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sa17/grand_tour.py", line 51, in <module>
    print(names[50])
IndexError: list index out of range
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
>>> 
>>> f = open('notes/hamlet.txt')
>>> 
>>> f = open('notes/hamlet.txtx')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    f = open('notes/hamlet.txtx')
FileNotFoundError: [Errno 2] No such file or directory: 'notes/hamlet.txtx'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
['Cisco', 'Samsung']
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
['Cisco', 'Samsung']
['Apple', 'Nvidia']
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
>>> Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    f = open('notes/hamlet.txtx')
FileNotFoundError: [Errno 2] No such file or directory: 'notes/hamlet.txtx
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
['Apple', 'Nvidia']
>>> 
>>> s = 'Samsung Rocks'
>>> len(s)
13
>>> s[0]
'S'
>>> s[12]
's'
>>> s[13 - 1]
's'
>>> s[len(s) - 1]
's'
>>> s[-1]
's'
>>> s[12]
's'
>>> s[-1]
's'
>>> s = 'Samsung Rocks'
>>> s[11]
'k'
>>> s[-2]
'k'
>>> s[:7]
'Samsung'
>>> s[8:]
'Rocks'
>>> s[-5:]
'Rocks'
>>> 
>>> 
>>> 
>>> s = 'index.html'
>>> s[5]
'.'
>>> s[:5]
'index'
>>> s[5:]
'.html'
>>> s[-5]
'.'
>>> s[:-5]
'index'
>>> s[-5:]
'.html'
>>> 
>>> s[:5], s[-5:]
('index', '.html')
>>> 
>>> s[:5], s[5:]
('index', '.html')
>>> s[:-5], s[-5:]
('index', '.html')
>>> 
>>> s = 'download.html'
>>> s[:5], s[-5:]
('downl', '.html')
>>> s[:5], s[5:]
('downl', 'oad.html')
>>> s[:-5], s[-5:]
('download', '.html')
>>> s = 'www.samsung.com'
>>> s[:-3]
'www.samsung.'
>>> s[-3:]
'com'
>>> s = 'www.hp.com'
>>> s[:-3]
'www.hp.'
>>> s[-3:]
'com'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
['Apple', 'Nvidia']
None
>>> 30
30
>>> None
>>> names.sort()
>>> names
['Apple', 'Cisco', 'Nvidia', 'Qualcomm', 'Samsung']
>>> 
>>> 
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> # Channeling Guido.
>>> 
>>> # But   So
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
['Apple', 'Nvidia']
None
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
['Apple', 'Nvidia']
None
['Apple', 'Cisco', 'Nvidia', 'Qualcomm', 'Samsung']
>>> 
>>> 
>>> 
>>> s = [(37, 'karthik'), (5, 'walle'), (32, 'mahe')]
>>> 
>>> sorted(s)
[(5, 'walle'), (32, 'mahe'), (37, 'karthik')]
>>> s
[(37, 'karthik'), (5, 'walle'), (32, 'mahe')]
>>> s.sort()
>>> s
[(5, 'walle'), (32, 'mahe'), (37, 'karthik')]
>>> 
>>> 
>>> # sorted(s) produces a NEW list, keeping the input intact
>>> #    the hint that you got new data is it returns a value
>>> s = [(37, 'karthik'), (5, 'walle'), (32, 'mahe')]
>>> sorted(s)
[(5, 'walle'), (32, 'mahe'), (37, 'karthik')]
>>> # s.sort() returns NONE,
>>> #    hint that the list was mutated
>>> s.sort()
>>> s
[(5, 'walle'), (32, 'mahe'), (37, 'karthik')]
>>> 
>>> s = 'the tale of two cities'
>>> s.replace('two', 'three')
'the tale of three cities'
>>> s
'the tale of two cities'
>>> 
>>> 
>>> t = s.replace('two', 'three')
>>> 
>>> s
'the tale of two cities'
>>> t
'the tale of three cities'
>>> 
>>> x = 10
>>> x + 1
11
>>> x
10
>>> x = x + 1
>>> s = 'the tale of two cities'
>>> s.replace('two', 'three')
'the tale of three cities'
>>> s
'the tale of two cities'
>>> s = s.replace('two', 'three')
>>> 
>>> 
>>> x = x + 1
>>> s = s.replace('two', 'three')
>>> 
>>> 
>>> # "Let's"  -> "Let us"  --> "Start typing"
>>> 
>>> 
>>> 'five' > 4
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    'five' > 4
TypeError: '>' not supported between instances of 'str' and 'int'
>>> sorted([10, 'five', 2])
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    sorted([10, 'five', 2])
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 
>>> 
>>> # BUT!
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
['Apple', 'Nvidia']
None
['Apple', 'Cisco', 'Nvidia', 'Qualcomm', 'Samsung']
<class 'dict'>
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
['Apple', 'Nvidia']
None
['Apple', 'Cisco', 'Nvidia', 'Qualcomm', 'Samsung']
<class 'dict'>
3
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
['Apple', 'Nvidia']
None
['Apple', 'Cisco', 'Nvidia', 'Qualcomm', 'Samsung']
<class 'dict'>
3
True
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
['Apple', 'Nvidia']
None
['Apple', 'Cisco', 'Nvidia', 'Qualcomm', 'Samsung']
<class 'dict'>
3
True
False
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
['Apple', 'Nvidia']
None
['Apple', 'Cisco', 'Nvidia', 'Qualcomm', 'Samsung']
<class 'dict'>
3
True
False
pc
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
['Apple', 'Nvidia']
None
['Apple', 'Cisco', 'Nvidia', 'Qualcomm', 'Samsung']
<class 'dict'>
3
True
False
pc
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sa17/grand_tour.py", line 81, in <module>
    print(computer['mary'])
KeyError: 'mary'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
['Apple', 'Nvidia']
None
['Apple', 'Cisco', 'Nvidia', 'Qualcomm', 'Samsung']
<class 'dict'>
3
True
False
pc
Mary had a little lamb
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
['Apple', 'Nvidia']
None
['Apple', 'Cisco', 'Nvidia', 'Qualcomm', 'Samsung']
<class 'dict'>
3
True
False
pc
Mary had a little lamb
Whose fleece was as white as snow
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
['Apple', 'Nvidia']
None
['Apple', 'Cisco', 'Nvidia', 'Qualcomm', 'Samsung']
<class 'dict'>
3
True
False
pc
Mary had a little lamb
Whose fleece was as white as snow
pc
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
['Apple', 'Nvidia']
None
['Apple', 'Cisco', 'Nvidia', 'Qualcomm', 'Samsung']
<class 'dict'>
3
True
False
pc
Mary had a little lamb
Whose fleece was as white as snow
pc
everywhere mary went, the lamb was sure to go
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
['Apple', 'Nvidia']
None
['Apple', 'Cisco', 'Nvidia', 'Qualcomm', 'Samsung']
<class 'dict'>
3
True
False
pc
Mary had a little lamb
Whose fleece was as white as snow
pc
everywhere mary went, the lamb was sure to go
>>> yans_car.price
'expensive'
>>> raymonds_car.price
'expensive'
>>> 
>>> yans_car.color
'Blue'
>>> raymonds_car.color
'Red'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
['Apple', 'Nvidia']
None
['Apple', 'Cisco', 'Nvidia', 'Qualcomm', 'Samsung']
<class 'dict'>
3
True
False
pc
Mary had a little lamb
Whose fleece was as white as snow
pc
everywhere mary went, the lamb was sure to go
>>> pprint(dict(vars(MercedesBenz)))
{'__dict__': <attribute '__dict__' of 'MercedesBenz' objects>,
 '__doc__': None,
 '__module__': '__main__',
 '__weakref__': <attribute '__weakref__' of 'MercedesBenz' objects>,
 'classy': True,
 'gas_mileage': 'terrible',
 'price': 'expensive'}
>>> 
>>> pprint(dict(vars(raymonds_car)), width=30)
{'color': 'Red',
 'gas_tank': 'Half'}
>>> pprint(dict(vars(yans_car)), width=30)
{'color': 'Blue',
 'gas_tank': 'Full'}
>>> 
>>> 
>>> yans_car.color
'Blue'
>>> yans_car.classy
True
>>> # Shared information is in the class
>>> # Unique information is in the instances
>>> # No redundancy
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
['Apple', 'Nvidia']
None
['Apple', 'Cisco', 'Nvidia', 'Qualcomm', 'Samsung']
<class 'dict'>
3
True
False
pc
Mary had a little lamb
Whose fleece was as white as snow
pc
everywhere mary went, the lamb was sure to go
dict_keys(['raymond', 'rachel', 'matthew'])
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
['Apple', 'Nvidia']
None
['Apple', 'Cisco', 'Nvidia', 'Qualcomm', 'Samsung']
<class 'dict'>
3
True
False
pc
Mary had a little lamb
Whose fleece was as white as snow
pc
everywhere mary went, the lamb was sure to go
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sa17/grand_tour.py =========
Hello, my name is __main__
What I like to do is
 Fast whirlwind tour of most of Python.
    No time to stop and linger.

Woohoo, I was run directly
<class 'function'>
121
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
[15, 11, 13, 21, 35, 55, 81, 113, 151, 195]
<class 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
4
['Cisco', 'Samsung', 'Qualcomm', 'Apple', 'Nvidia']
Cisco
Oops, I did it again. I indexed too far. I am not that innocent
Cisco
Nvidia
['Cisco', 'Samsung']
['Apple', 'Nvidia']
Nvidia
Apple
['Cisco', 'Samsung']
['Apple', 'Nvidia']
None
['Apple', 'Cisco', 'Nvidia', 'Qualcomm', 'Samsung']
<class 'dict'>
3
True
False
pc
Mary had a little lamb
Whose fleece was as white as snow
pc
everywhere mary went, the lamb was sure to go
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sa17/download1.py ==========
=================================== Source: http://172.16.0.73:8080/sa17/links.txt ==================================
                                    Starting download at Mon Oct 29 16:57:35 2018                                    
304  Not Modified     http://172.16.0.73:8080/sa17/download.py
304  Not Modified     http://172.16.0.73:8080/sa17/links.txt
304  Not Modified     http://172.16.0.73:8080/sa17/getting_setup.py
304  Not Modified     http://172.16.0.73:8080/sa17/c_arrays_vs_python_lists.py
304  Not Modified     http://172.16.0.73:8080/sa17/overview.py
304  Not Modified     http://172.16.0.73:8080/sa17/how_for_loops_work.py
304  Not Modified     http://172.16.0.73:8080/sa17/grand_tour.py
304  Not Modified     http://172.16.0.73:8080/shared/picirc.py
304  Not Modified     http://172.16.0.73:8080/shared/banner.py
304  Not Modified     http://172.16.0.73:8080/shared/norvig_corrector.py
304  Not Modified     http://172.16.0.73:8080/shared/corpus.dat
304  Not Modified     http://172.16.0.73:8080/shared/highlight.py
304  Not Modified     http://172.16.0.73:8080/shared/publish.py
304  Not Modified     http://172.16.0.73:8080/shared/words.txt
304  Not Modified     http://172.16.0.73:8080/shared/fsm.py
304  Not Modified     http://172.16.0.73:8080/shared/__init__.py
304  Not Modified     http://172.16.0.73:8080/shared/BeautifulSoup.py
304  Not Modified     http://172.16.0.73:8080/shared/pexpect.py
304  Not Modified     http://172.16.0.73:8080/shared/oop_story.txt
304  Not Modified     http://172.16.0.73:8080/shared/bottle.py
304  Not Modified     http://172.16.0.73:8080/shared/PythonAwesome.pdf
304  Not Modified     http://172.16.0.73:8080/shared/islands.pdf
304  Not Modified     http://172.16.0.73:8080/shared/queue_stats.txt
304  Not Modified     http://172.16.0.73:8080/shared/crossword_challenge.py
304  Not Modified     http://172.16.0.73:8080/shared/ipv4_int_bri.txt
304  Not Modified     http://172.16.0.73:8080/shared/show_controllers.txt
304  Not Modified     http://172.16.0.73:8080/shared/raisin_team.csv
304  Not Modified     http://172.16.0.73:8080/shared/raisin_team_update.csv
304  Not Modified     http://172.16.0.73:8080/shared/books.json
304  Not Modified     http://172.16.0.73:8080/shared/books.xml
304  Not Modified     http://172.16.0.73:8080/shared/rss.xml
304  Not Modified     http://172.16.0.73:8080/shared/fruit.xml
304  Not Modified     http://172.16.0.73:8080/shared/stocks.txt
304  Not Modified     http://172.16.0.73:8080/shared/email.txt
304  Not Modified     http://172.16.0.73:8080/shared/dns_servers.json
304  Not Modified     http://172.16.0.73:8080/shared/team_history.json 
304  Not Modified     http://172.16.0.73:8080/shared/team_history.txt
304  Not Modified     http://172.16.0.73:8080/shared/re.txt
304  Not Modified     http://172.16.0.73:8080/shared/hamlet.txt
304  Not Modified     http://172.16.0.73:8080/shared/nasa_19950801.log
304  Not Modified     http://172.16.0.73:8080/shared/call_by_object.txt
>>> # http://bit.ly/python-sa17
>>> 
