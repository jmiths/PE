#!/usr/bin/python3

# x^2 - D * y^2 = 1

import math

big_x = 0
big_d = 0
for d in range(1,1001):
    if math.sqrt(d).is_integer():
        continue
    found = False
    y = 1
    while found == False:
        x = math.sqrt((d * y**2) + 1)
        if x.is_integer():
            if x > big_x:
                big_x = x
                big_d = d
            print(int(x),d,y)
            found = True
        y = y+1
print(big_d)
