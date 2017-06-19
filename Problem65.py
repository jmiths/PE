#!/usr/bin/python
'''
from fractions import *
import sys
def find_cont(num):
#    return 2
    if num % 3 == 2:
        return (2*((num)/3))+2
    else:
        return 1

#for i in range(1,15):
#    print find_cont(i)

def find_pred(n,stop):
    if (n == stop):
        return find_cont(n)
    else:
        #print find_cont(n), n, stop
        #print "Frac: ", Fraction(1/find_pred(n+1,stop))
        return find_cont(n) + Fraction(1./find_pred(n+1,stop))

for end in range(1,10):
    score = 0
    temp = Fraction(2 + 1./find_pred(1,end))
    print temp
#    temp = str(temp.numerator)
#    for char in temp:
#        score += int(char)
#    print score
'''

'''
Used Maple for arbitary precision:
with(numtheory);
cfrac(exp(1),100,'poop');
poop[100] and take num and add in python    
'''
