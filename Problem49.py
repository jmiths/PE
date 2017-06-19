#!/usr/bin/python

# I only need 10000 primes

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
#		max_iter = math.log(len(primes),num)
#		print "num: " + str(num) + " max_iter: " + str(max_iter)
		for bad_val in range(num*num,len(primes),num):
			primes[bad_val] = 0

for num in range(1000,10000):
	if primes[num] == 1:
		lex_sort = str(''.join(sorted(str(num))))
		if lex_sort in finding:
			finding[lex_sort].append(num)
		else:
			finding[lex_sort] = [num]

for key in finding:
	if len(finding[key]) >= 3:
		lis = finding[key]
		for i in range(0,len(lis)):
			if i+1 == len(lis):
				break
			for j in range(i+1,len(lis)):
				if j+1 == len(lis):
					break
				for k in range(j+1,len(lis)):
					if lis[k]-lis[j] == lis[j]-lis[i]:
						print str(lis[i]) + " " + str(lis[j]) + " " + str(lis[k])
