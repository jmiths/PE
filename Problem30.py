#!/usr/bin/python

quick_math = {}

for i in range(0,10):
	quick_math[str(i)] = i**5
'''
1^5: 1
2^5: 32
3^5: 243
4^5: 1024
5^5: 3125
6^5: 7776
7^5: 16807
8^5: 32768
9^5: 59049
'''

big_one = 0

for i in range(2,1000000):
	str_ed = str(i)
	summer = 0
	for blah in str_ed:
		summer += quick_math[blah]
	if summer == i:
		print i
		big_one += i

print big_one
