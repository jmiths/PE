#!/usr/bin/python3

'''
Sums:
1: 1
2: 2
3: 2
4: 4
5: 6
6: 10
...
'''

n = 100
a = [0] * (n+1)
a[0] = 1

for i in range(1,n):
        for j in range(i,n+1):
                a[j] += a[j-i]
print(a[-1])
