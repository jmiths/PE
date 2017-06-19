#!/usr/bin/python
from fractions import *
import sys
sys.setrecursionlimit(1500)
'''
No known sequence
num         Delta
1   3       
2   7       4
3   17      10
4   41      24
5   99      58
6   239     140
7   577     338
8   1393    816

demon
1   2
2   5       3
3   12      7
4   29      17
5   70      41
6   169     90
7   408     239
8   985     577
'''
count = 0
def find_pred(n):
    if (n == 0):
        return 2
    else:
        return 2 + Fraction(1/find_pred(n-1))

for i in range(1,1001):
    temp = Fraction(1 + 1/find_pred(i))
    d = len(str(temp.denominator))
    n = len(str(temp.numerator))
    if n > d:
        count += 1

print count
