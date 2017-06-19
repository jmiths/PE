#!/usr/bin/python

import sys

primes = [1]*10000000
primes[0] = 0
arr = []
for index in range(len(primes)):
    if primes[index] == 0:
        continue
    else:
        for bad_val in range(index*(2+(2*index)),len(primes),2*index+1):
            primes[bad_val] = 0

for index in range(len(primes)):
    if primes[index] == 1:
        arr.append(2*index+1)

for i in reversed(arr):
    found = True
    temp = str(i)
    bit = [0] * 10
    for char in temp:
        bit[int(char)] += 1
    for ind in range(1,len(temp)+1):
        if bit[ind] != 1:
            found = False
    if found == True:
        print i
        sys.exit()
