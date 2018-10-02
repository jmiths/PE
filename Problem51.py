#!/usr/bin/python

import math

primes = [1]*500000
primes[0] = 0
print("Last Prime:  " + str(2*len(primes)))
lower_limit = 100000
print("Lower Limit: " + str(lower_limit))

for index in range(len(primes)):
    if primes[index] == 0:
	continue
    else:
	for bad_val in range(index*(2+(2*index)),len(primes),2*index+1):
	    primes[bad_val] = 0

p=[]
for index in range(len(primes)):
    if primes[index] == 1:
        pri = 2*index+1
        if pri >= lower_limit:
            p.append(str(pri))

print("Generating")
sto = {}
for i in p:
    for a in range(len(i)):
        for b in range(a+1,len(i)):
            if i[a] == i[b]:
                temp = i
                temp = temp[0:a]+"x"+temp[a+1:b]+"x"+temp[b+1:]
                if temp in sto:
                    sto[temp] = sto[temp] + 1
                else:
                    sto[temp] = 1
                for c in range(b+1,len(i)):
                    if i[b] == i[c]:
                        temp = i
                        temp = temp[0:a]+"x"+temp[a+1:b]+"x"+temp[b+1:c]+"x"+temp[c+1:]
                        if temp in sto:
                            sto[temp] = sto[temp] + 1
                        else:
                            sto[temp] = 1
print("Searching")
for key in sto:
    if sto[key] >= 8:
        print(key + " " + str(sto[key]))
