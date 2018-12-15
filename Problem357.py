#!/usr/bin/python3
'''
for all divisors d
n > 100 000 000
d+(n/d)

Can only be even numbers for this problem

All primes from 100 000 000/2
Go from prime factors to divisors

For instance 30
1 and 30 assumed
2 3 5
All of these divisions, still make an odd, 30/odd + odd = odd
30 / even + even = odd

28
1 and 28
2 2 7
7 -> 7 + (28/7) -> 11
14 -> 14 + 28/14 -> 21
2 -> 2 + (28/2) -> 16
28 / even + even = even
28 / odd + odd = doesn't matter

Must test numbers that are odds * 2
'''

import math

primes = [1]*100000000
primes[0] = 0

for index in range(len(primes)):
	if primes[index] == 0:
		continue
	else:
		for bad_val in range(index*(2+(2*index)),len(primes),2*index+1):
			primes[bad_val] = 0
prime = {}
for index in range(len(primes)):
    if primes[index] == 1:
      prime[2*index+1] = True
total = 0
for i in range(1,50000000,2):
      t = i * 2
      prime_gen = True
      for d in range(1,int(math.sqrt(t)+1)):
         if t % d == 0:
            if d + (t/d) not in prime:
               prime_gen = False
               break
      if prime_gen == True:
         total += i*2
total += 1
print(total)
