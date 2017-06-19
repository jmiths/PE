#!/usr/bin/python
import math


def check_prime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

sides = 1
prime = 0
tries = 1.0
for n in range(2,10000000):
    sides += 2
    tries += 4.0
#    print ("Side: ", sides)
#    print 4*(n**2)-10*n+7
#    print 4*n**2-8*n+5
#    print 4*n**2-6*n+3
#    print (2*n-1)**2
    if check_prime(4*(n**2)-10*n+7):
        prime += 1
    if check_prime(4*n**2-8*n+5):
        prime += 1
    if check_prime(4*n**2-6*n+3):
        prime += 1
    if check_prime((2*n-1)**2):
        prime += 1
    if (prime/tries < .1):
        print sides
        break
