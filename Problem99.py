#!/usr/bin/python

import math
it = 1
line_num = 0
maxi = 0
with open("p99.txt") as f:
    for line in f:
        temp = line.rstrip().split(",")
        val = (int(temp[1]) * math.log(int(temp[0]))) / math.log(10)
        if val > maxi:
            maxi = val
            line_num = it
        it = it + 1
print(line_num)
#(exp * math.log(base)) / math.log(10)
