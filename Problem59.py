#!/usr/bin/python

import itertools

file = open("p059_cipher.txt",'r')
for line in file:
    line = line.strip()
    lis = line.split(',')

first_lis = lis[0::3]
second_lis = lis[1::3]
third_lis = lis[2::3]

#print np.cross(list(range(97,123)),list(range(97,123)))

tries = []
for num1 in range(97,123):
    for num2 in range(97,123):
        for num3 in range(97,123):
            tries.append([num1,num2,num3])

for key in tries:
    str = ""
    for num in range(len(third_lis)):
        str += chr(key[0] ^ int(first_lis[num]))
        str += chr(key[1] ^ int(second_lis[num]))
        str += chr(key[2] ^ int(third_lis[num]))
    if str.find("the") != -1 and str.find("be") != -1 and str.find("and") != -1:
        score = 0
        for i in first_lis:
            score += key[0] ^ int(i)
        for i in second_lis:
            score += key[1] ^ int(i)
        for i in third_lis:
            score += key[2] ^ int(i)
        print score
        print str

#for num in range(97,123):
#    found = True
#    for i in first_lis:
#        temp = int(i)
#        decr = temp ^ num
#        print decr
#        if decr != 32 or not (decr > 96 and decr < 123) or not (decr > 64 and decr < 91):
#            print decr
#            found = False
#            break
#    if (found == True):
#        print num
        
