#!/usr/bin/python
from fractions import Fraction
# 3/7 -> 3 000 000 / 7 000 000

# 3/7 * 1000000 = 428571.4285714285

# 428571 / 1 000 000 no...?

limit = 3.0/7.0
winner = 0.4
ind = 0
dem = 0
limit2 = Fraction(7,3)
for d in range(1,1000000):
    for n in range(int(d*winner),d):
        blah = n/float(d)
        if blah > limit:
            break
        if blah > winner and Fraction(d,n) != limit2:# and blah < limit:
            winner = blah
            ind = n
            dem = d
print ind, dem
