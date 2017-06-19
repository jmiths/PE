#!/usr/bin/python
from fractions import *

limit = Fraction(3,7)

for i in range(1000000,0,-1):
    temp = limit - Fraction(1,i)
    if (temp.denominator < 1000000):
        print(temp.numerator)
        quit()
