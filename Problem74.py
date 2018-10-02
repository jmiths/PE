#!/usr/bin/python3

import math

facts = {}
for i in range(0,10):
    facts[str(i)] = math.factorial(i)

print(facts)
total = 0
for i in range(1,1000000):
    seen = {}
    seen[i] = 0
    it = 1
    temp = str(i)
    nex = 0
    while it < 70:
        for j in range(len(temp)):
            nex = nex + facts[temp[j]]
        if nex in seen:
            #print (str(i) + " : " + str(it))
            #print(seen)
            if it == 60:
                print(i)
                total = total + 1
            break
        else:
            seen[nex] = it
        it = it + 1
        temp = str(nex)
        nex = 0
print(total)
