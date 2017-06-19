#!/usr/bin/python

import math

primes = [1]*301
primes[0] = 0

'''
Sieve primes using only odd numbers by reducing values to index
based on formula: Value = (2 * Index_val) + 1. Squares of these values
can be found at Index_Sq = Index_val * ( 2 + ( 2 * Index_val)). 

This was arrived at by starting with a bit-vector of all numbers from 0 to N
we applied a sieve, which used too much space. An observation was made that all even numbers, excluding 2, were not prime. In order to eliminate all even numbers from consideration
we wrote out the remaining numbers and their indicies and determined that the index of their associated square existed at an index following a recognizable pattern: (1,4)(2,12)(3,24)
Therefore, we can start at the exponent and walk the indexes value to eliminate all multiples of that value
'''

for index in range(len(primes)):
	if primes[index] == 0:
		continue
	else:
		for bad_val in range(index*(2+(2*index)),len(primes),2*index+1):
			primes[bad_val] = 0

for index in range(len(primes)):
    if primes[index] == 1:
      print 2*index+1
