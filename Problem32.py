#!/usr/bin/python

score = 0
products = []

for m in range(1,100):
    for n in range(100,10000):
        found =  True
        temp = str(m * n) + str(m) + str(n)
        bit = [0] * 10
        for char in temp:
            bit[int(char)] += 1
        if bit[0] != 0:
            continue
        for i in range(1,len(bit)):
            if bit[i] != 1:
                found = False
        if found == True:
            if (m*n) not in products:
                products.append(m*n)
                score += (m*n)
print score
