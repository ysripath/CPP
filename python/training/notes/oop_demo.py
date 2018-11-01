'Fundamental of Object Oriented Programming'

from pprint import pprint

class Demo:

    status = 'Not for resale'

class Merchandise:

    status = 'For sale'

class Electronics:

    core_functionality = 'Manipulates the flow of electrons'

class CircuitBoard(Demo):
    'Arrangement of electronic components'

    kind = 'Surface mount'

    color = 'green'

    def __init__(self, name, design):
        self.name = 'Radio'
        self.design = 'Superheterodyne'

class Component(Merchandise, Electronics):
    'Specifications for an electronic component'

    kind = 'Prototype'

    color = 'black'

    location = 'San Jose'

    def __init__(self, partnum, desc, color=None):
        self.partnum = partnum
        self.desc = desc
        self.pinout = {}
        if color is not None:
            self.color = color

    def __getitem__(self, pin_number):
        return self.pinout[pin_number]

    def __setitem__(self, pin_number, connection):
        self.pinout[pin_number] = connection

    def __len__(self):
        return len(self.pinout)

    def __str__(self):
        return f'Component part number {self.partnum} is a {self.color} {self.desc.lower()}'

    def __repr__(self):
        if self.color == Component.color:
            return f'Component(partnum={self.partnum!r}, desc={self.desc!r})'
        return f'Component(partnum={self.partnum!r}, desc={self.desc!r}, color={self.color!r})'
        
ra = CircuitBoard('Radio', 'Superheterodyne')

oa = Component('741', 'Operational Amplifier')
oa[2] = 'Inverting input'
oa[3] = 'Non-inverting input'
oa[4] = 'Ground 2A max'
oa[6] = 'Signal 8 ohms'
oa[7] = 'Vcc +5V'

tm = Component('555', 'Timer')
tm[1] = 'Ground 2A max'
tm[2] = 'Trigger'
tm[3] = 'Signal 8 ohms'
tm[4] = 'Reset'
tm[5] = 'Vcc +5V'
tm[6] = 'Threshold'

ps = Component('PS191', 'Power Supply', 'blue')
ps[2] = 'Vcc +5V'
ps[7] = 'Ground 2A max'
ps[3] = 'Emergency shutoff'

lp = Component('TLC04ID', 'Active Loss-pass Filter')
lp[2] = 'Vcc +5V'
lp[5] = 'Ground 2A max'
lp[6] = 'Signal 8 ohms'
lp[7] = 'Threshold'

assert oa[6] == tm[3]
assert lp[5] == ps[7]
assert tm[3] == lp[6]
assert ps[2] == tm[5]

parts = [oa, tm, ps, lp]
for part in parts:
    print(part.kind, part.color, part.partnum, part.desc)

print(oa)
print(repr(oa))

