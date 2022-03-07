a = 5
print(type(a))
c = 2 + 5j
print(type(c))
print(isinstance(c,complex))
print(isinstance(a,complex))
print(c+4)
print(c+3j)

print(0b1101101)
print(0o1234567)
print(0xf)

print(1.1 + 2.2)
import decimal
print(0.1)
print(decimal.Decimal(1.1))
from decimal import Decimal as D
print(D('1.1') + D('2.2'))
print(D('1.2') * D('2.50'))

import fractions
print(fractions.Fraction(1.5))
print(fractions.Fraction(5))
print(fractions.Fraction(1,3))

print(fractions.Fraction(1.1))
print(fractions.Fraction('1.1'))

from fractions import Fraction as F
print(F(1, 3) + F(1, 3))
print(1 / F(5, 6))
print(F(-3, 10) > 0)
print(F(-3, 10) < 0)

import math
print(math.pi)
print(math.cos(math.pi))
print(math.exp(10))
print(math.log10(1000))
print(math.sinh(1))
print(math.factorial(100))

import random
print(random.randrange(10, 20))
x = ['a', 'b', 'c', 'd', 'e']
print(random.choice(x))
random.shuffle(x)
print(x)
print(random.random())
