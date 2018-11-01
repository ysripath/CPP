''' Fast whirlwind tour of most of Python.
    No time to stop and linger.
'''

print('Hello, my name is', __name__)
print('What I like to do is',)
print(__doc__)

if __name__ == '__main__':
    print('Woohoo, I was run directly')
else:
    print('Oh no! I was imported')

##################################################
# How to make functions

def square(x):
    'Return a value times itself'
    return x * x

print(type(square))
print(square(11))
print([square(0), square(1), square(2), square(3), square(4),
       square(5), square(6), square(7), square(8), square(9),
       square(10), square(11), square(12), square(13), square(14)])
print([square(x) for x in range(15)])
print(list(map(square, range(15) )))

print(list(map(lambda x: 3*x**2 - 7*x + 15, range(10))))
print([3*x**2 - 7*x + 15 for x in range(10)])

def show_info(func):
    "Display a function's attributes"
    print(f'The {func.__name__} {func.__class__.__name__} is defined in {func.__module__}:')
    print()
    print(f'\t{func.__doc__}')
    print()

#####################################################
# Lists

names = ['Cisco', 'Samsung', 'Qualcomm', 'Apple']

print(type(names))
print(dir(list))
print(len(names))
names.append('Nvidia')
print(names)
print(names[0])                 # zero-indexed 

try:
    print(names[50])
except IndexError:
    print('Oops, I did it again. I indexed too far. I am not that innocent')

print(names[0])                  # First name
print(names[len(names) - 1])     # Last name

print([names[0], names[1]])      # First two names
print([names[3], names[4]])      # Last two names

print(names[-1])                 # First name from the right
print(names[-2])                 # Second name from the right

print(names[:2])                 # First two names
print(names[-2:])                # Last two names

print(names.sort())              # Returning None is a hint that the data changed
print(names)

## Dictionaries ########################################

computer = {'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}

print(type(computer))
print(len(computer))
print('rachel' in computer)
print('smitha' in computer)
print(computer['rachel'])

# EAFP:  Easier to ask forgiveness than permission
try:
    print(computer['mary'])
except KeyError:
    print('Mary had a little lamb')

# LBYL: Look before you leap
if 'mary' in computer:
    print(computer['mary'])
else:
    print('Whose fleece was as white as snow')

# Unconditional lookup (never fails because you supply a default value)
print(computer.get('rachel', 'no computer'))
print(computer.get('mary', 'everywhere mary went, the lamb was sure to go'))

# Views of dictionary
print(computer.keys())
print(computer.values())
print(computer.items())

## Object Oriented Programming ##############################

from pprint import pprint

class MercedesBenz:

    price = 'expensive'

    gas_mileage = 'terrible'

    classy = True

yans_car = MercedesBenz()
yans_car.color = 'Blue'
yans_car.gas_tank = 'Full'

raymonds_car = MercedesBenz()
raymonds_car.color = 'Red'
raymonds_car.gas_tank = 'Half'

## String Formatting ######################################

new = 10
old = 20
print('The answer is %d today but was %d yesterday' % (new, old))
print('The answer is %(new)d today but was %(old)d yesterday' % {'old': old, 'new': new})
print('The answer is {0} today but was {1} yesterday'.format(new, old))
print('The answer is {new} today but was {old} yesterday'.format(old=old, new=new))
print(f'The answer is {new} today but was {old} yesterday')

## Encodings ##############################################

# Things you can use       o--(encoding)-->             Things you can move or store
#                          <--(decoding)--o

# Encoder / Decoder pair is called a "codec"

# Voice               --(mp3, au, aiff, wav)-->         bytes (numbers in the range 0 <= x < 256)
# Unicode             --(latin-1, utf-8, ...)-->        bytes
# Dictionary          --(yaml, json, xml, url)-->       bytes

story = '\N{snowman}\N{umbrella}\N{comet}'
raymond_way = 'TheRaymondWay\N{trade mark sign}'
math_stuff = 'lim x\N{long rightwards arrow}\N{infinity}, sin\N{superscript two}(x)'

sb = story.encode('utf-8')
rb = raymond_way.encode('utf-16')
mb = math_stuff.encode('utf-32')

print(sb.decode('utf-8'))
print(rb.decode('utf-16'))
print(mb.decode('utf-32'))

pref = dict(raymond='red', rachel='blue', matthew='yellow', numtwo='green')
print(pref['rachel'])

import json, pickle, marshal, urllib.parse

s1 = json.dumps(pref)
s2 = pickle.dumps(pref)
s3 = marshal.dumps(pref)
s4 = urllib.parse.urlencode(pref)

d1 = json.loads(s1)
d2 = pickle.loads(s2)
d3 = marshal.loads(s3)
d4 = urllib.parse.parse_qs(s4)

print(d1)
print(d2)
print(d3)
print(d4)

## Sets ###############################################################

s = {10, 20, 30, 40, 30, 20, 10}
print(type(s))
print(dir(s))
print(len(s))                           #1 use case for sets is uniquification or deduping
print(20 in s)                          #2 use case for sets is VERY FAST membership testing

t = {30, 40, 50, 60}
print(s.union(t))
print(s.intersection(t))
print(s.difference(t))
print(t.difference(s))

print(s | t)                            # "or" operator computes the union
print(s & t)                            # "and" operator computes the intersection
print(s - t)                            # "minus" operator computes the difference
print(t - s)                            # "minus" operator computes the difference

supported_extensions = {'html', 'css', 'php', 'xml', 'xhtml'}

url = 'http://www.samsung.us.com/fun/games/monopoly.php'
extension = url.split('.')[-1]
if extension in supported_extensions:
    print('Yes, we can!')
else:
    print("No we won't. #MPGA")

## How to open and close files ######################

f = open('notes/hamlet.txt')
try:
    play = f.read()
    print(len(play))
finally:
    f.close()

with open('notes/hamlet.txt') as f:
    play = f.read()
    print(len(play))

## How do urls work? ################################

import urllib.request

u = urllib.request.urlopen('http://www.jython.org')
try:
    page = u.read().decode('utf-8')
    print(len(page))
finally:
    u.close()

with urllib.request.urlopen('http://www.jython.org') as u:
    page = u.read().decode('utf-8')
    print(len(page))    










