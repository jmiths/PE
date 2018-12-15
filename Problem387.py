#!/usr/bin/python3
import math 

primes = [1]*1000000
primes[0] = 0

for index in range(len(primes)):
   if primes[index] == 0:
      continue
   else:
      for bad_val in range(index*(2+(2*index)),len(primes),2*index+1):
         primes[bad_val] = 0

prime = {2:True}

for index in range(len(primes)):
   if primes[index] == 1:
      prime[2*index+1] = True
prime_fac = prime.keys()

def is_prime(n):
   if n == 1:
      return False
   if n in prime: # If in our dict just return
      return True
   else:
      for ele in prime_fac: # Else use the dict to run through prime facs
         if ele > math.sqrt(n)+1:
            return True
         if n % ele == 0:
            return False
      for ele in range(1999993,int(math.sqrt(n)+1),2): # If we didn't generate enough then start at last prime facs and check up from there (saves 2.5 sseconds)
         if n % ele == 0:
            return False
   return True

prev = []
nex = []
c = 1
total = 0
while c < 15:
   if c == 1:
      for i in range(1,10):
         nex.append([str(i),i])
   else:
      for val in prev:
         old_int_val = int(val[0])
         sum_digit = val[1]
         strong = False
         if is_prime(old_int_val/sum_digit):
            strong = True
         for i in range(0,10):
            new_val = val[0] + str(i)
            int_new_val = int(new_val)
            if strong:
               if is_prime(int_new_val):
                  total += int_new_val
            if i != 0:
               sum_digit += 1
            if int_new_val%sum_digit == 0:
               nex.append([new_val,sum_digit])
   prev = nex
   nex = []
   c += 1
   #print(prev)
print(total)
