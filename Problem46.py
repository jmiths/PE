#!/usr/bin/python

import math

primes = [1]*10001
primes[0] = 0
primes[1] = 0

finding = {}

# print str(math.log(8,2)) 2^3 = 8. This prints 8.
for num in range(0,len(primes)):
	if primes[num] == 0:
		continue
	else:
		for bad_val in range(num*num,len(primes),num):
			primes[bad_val] = 0

for num in range(3,len(primes),2):
	if primes[num] == 1:
		continue
	found = False
	for prime in range(2,num):
		if primes[prime] == 1:
			if math.sqrt( ( num - prime ) / 2).is_integer():
				found = True
				break
	if found == False:
		print num
		exit(1)
