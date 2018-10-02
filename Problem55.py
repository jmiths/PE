#!/usr/bin/python3

def isPal(num):
    num = str(num)
    rev = num[::-1]
    for i in range(int(len(num)/2)+1):
        if num[i] != rev[i]:
            return False
    return True

def rev_sum(num):
    temp = str(num)
    rev = int(temp[::-1])
    return num + rev

total = 0
for i in range(1,10000):
    it = 0
    while it < 55:
        i = rev_sum(i)
        if isPal(i):
            total = total + 1
            break
        it = it + 1
print(9999-total)
