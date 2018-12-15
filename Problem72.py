#!/usr/bin/python3
import math

n = 1001

frac = {}

def redux(num,denom):
        l = math.gcd(num,denom)
        while l != 1:
                num = int(num / l)
                denom = int(denom / l)
                l = math.gcd(num,denom)
        return str(num)+"/"+str(denom)

for i in range(2,n):
   if i % 10000 == 0:
      print(i)
   for j in range(2,i):
      a = redux(j,i)
      if a not in frac:
         frac[a] = True
print(frac.keys())
print(len(frac.keys()))
