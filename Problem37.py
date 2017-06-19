#!/usr/bin/python

import math

primes = [1]*1000001
primes[0] = 0

sum = 23


for index in range(len(primes)):
    if primes[index] == 0:
        continue
    else:
        for bad_val in range(index*(2+(2*index)),len(primes),2*index+1):
            primes[bad_val] = 0

evens = set('02468')
for index in range(5,len(primes)):
    if primes[index] == 0:
        continue
    num = 2*index+1
    if any((c in evens) for c in str(num)):
        continue
    bad = False
    for i in range(1,len(str(num))):
        from_left = int(str(num)[0: len(str(num))-i])
        from_right = int(str(num)[i: len(str(num))])
    #    print str(from_left) + " " + str(from_right)
        if primes[(from_left-1)/2] != 1 or primes[(from_right-1)/2] != 1:
            bad = True
            break
    if bad == False:
        sum += num
print sum
