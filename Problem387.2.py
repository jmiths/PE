#!/usr/bin/python

import math

primes = [1]*10001
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
with open('harshad_test') as f:
   for line in f:
      a = int(line.strip())
      if a in prime:
         print(a, " is prime")
         total += a
print(total)
