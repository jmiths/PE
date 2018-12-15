#!/usr/bin/python3

bouncies = 0
for i in range(100,10000000):
        temp = list(str(i))
        temp2 = sorted(temp)
        if temp != temp2 and temp != temp2[::-1]:
                bouncies += 1
        if bouncies/i >= .99:
                print(i)
                exit(0)
#        if i % 1000 == 0:
#                print(i, " ", bouncies/i)
