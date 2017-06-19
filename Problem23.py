#!/usr/bin/python

# Primes by default are not abundant

import math, itertools
from sets import Set

#primes = [1]*28125
#primes[0] = 0
#primes[1] = 0

#for num in range(0,len(primes)):
#	if primes[num] == 0:
#		continue
#	else:
#		for bad_val in range(num*num,len(primes),num):
#			primes[bad_val] = 0

#abun = []
#for num in range(11,len(primes)):
#    if primes[num] == 0:
#        abun.append(num)

#abun_score = {}
abuns = []
for num in range(11,28123):
    score = 1
    for div in range(2,(num/2)+1):
        if num % div == 0:
            val = num / div
            if val > div:
                score = score + div + val
            elif val == div:
                score += div
    if score > num:
        abuns.append(num)
#print abuns
cross = list(itertools.product(abuns,abuns))
score = 0
print len(cross)
big_set = Set([])
for element in cross:
    big_set.add(element[0] + element[1])

for num in range(1,28124):
    if num not in big_set:
        score += num

print score

'''
for num in range(1,28124):
    found = False
    for num1 in abuns:
        if found == True:
            break
        if num1 > num:
            break
        for num2 in abuns:
            if num1 + num2 == num:
                found = True
                break
            if num2 > num:
                break
            if num1 + num2 > num:
                break
    if found == False:
        score += num

print score
'''
