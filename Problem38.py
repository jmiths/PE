#!/usr/bin/python

max  = 918273645

for i in range(9182,10000):
    found = True
    temp = i*2
    temp = str(i) + str(temp)
    bit = [0] * 10
    for char in temp:
        bit[int(char)] = 1
    for i in range(1,len(bit)):
        if bit[i] != 1:
            found = False
    if found == True:
        if int(temp) > max:
            max = int(temp)
print max
