#!/usr/bin/python3

import math

primes = [1]*500000
primes[0] = 0
p = [2]


for index in range(len(primes)):
	if primes[index] == 0:
		continue
	else:
		for bad_val in range(index*(2+(2*index)),len(primes),2*index+1):
			primes[bad_val] = 0

for index in range(len(primes)):
    if primes[index] == 1:
       p.append(2*index+1)

total = 1
for i in p:
    if i*total > 1000000:
        break
    else:
        total = total * i
print(total)
