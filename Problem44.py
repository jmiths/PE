#!/usr/bin/python

pent = []
pentd = {}

d = 100000000

for i in range(1,10000):
    pent.append((i* (3*i-1) )/2)
    pentd[(i* (3*i-1) )/2] = True

for i in range(len(pent)):
    for j in range(i,len(pent)):
        temp = pent[i]
        temp2 = pent[j]
        sub = abs(temp - temp2)
        if temp + temp2 in pentd and sub in pentd:
            if sub < d:
                d = sub
                print d

