#!/usr/bin/python

import math

literal_shit = {}

for i in range(2,10000):
    for j in range(i,11000):
        temp = math.sqrt(i**2 + j**2)
        if temp.is_integer():
            len = int(i+j+temp)
            if i+j+temp < 1500000:
                if len in literal_shit:
                    literal_shit[len] += 1
                else:
                    literal_shit[len] = 1
                print i, j, temp, "len:", len
            else:
                break

for key in literal_shit:
    print key, literal_shit[key]
