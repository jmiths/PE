#!/usr/bin/python3
import math

n = 12001

frac = {}

def start(i):
        a = int(math.floor(i/3))
        if a/i <= (1/3):
                return a+1
        else: 
                return a

def end(i):
        a = int(math.floor(i/2))
        if a/i < (1/2):
                return a+1
        else:
                return a

def redux(num,denom):
        l = math.gcd(num,denom)
        while l != 1:
                num = int(num / l)
                denom = int(denom / l)
                l = math.gcd(num,denom)
        return str(num)+"/"+str(denom)

for i in range(4,n):
        for j in range(start(i),end(i)):
                a = redux(j,i)
                if a not in frac:
                       frac[a] = True
print(len(frac.keys()))
