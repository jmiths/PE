#!/usr/bin/python3

# x^2 - D * y^2 = 1

import math

squaring = {}
squares = {}
for n in range(1,10000000):
    temp = n**2
    squares[temp] = n
    squaring[n] = temp

big_x = 0
big_d = 0
not_found = []
for d in range(1,1001):
    if math.sqrt(d).is_integer():
        continue
    found = False
    for y in range(1,10000000):
        #for y in range(1,100000):
        x = (d * squaring[y]) + 1
        if x in squares:
            if squares[x] > big_x:
                big_x = squares[x]
                big_d = d
            print(d,squares[x],y)
            found = True
        if found == True:
            break
    if found == False:
        not_found.append(d)
        print("NOT FOUND AT: ",d)
print(not_found)
print(big_d)
