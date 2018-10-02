#!/usr/bin/python
#https://projecteuler.net/problem=99

import math
it = 1 # Line number tracking
line_num = 0 #Maximum number's line number
maxi = 0 # Maximum number
with open("p99.txt") as f: #Format is base , exponent
    for line in f:
        temp = line.rstrip().split(",")
        #Scaling applied to each number (exp * math.log(base)) / math.log(10)
        val = (int(temp[1]) * math.log(int(temp[0]))) / math.log(10)
        # Find max and update values if it is
        if val > maxi:
            maxi = val
            line_num = it
        it = it + 1
print(line_num)
