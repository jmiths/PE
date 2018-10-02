#!/usr/bin/python3

big_sto={}

for i in range(0,10000):
    a = [0]*10
    temp = str(i**3)
    for j in temp:
        ind = int(j)
        a[ind] = a[ind] + 1
    string = ""
    for elem in a:
        string = string + str(elem)
    if string in big_sto:
        big_sto[string][0] = big_sto[string][0] + 1
    else:
        big_sto[string] = [1,i]
for key in big_sto:
    if big_sto[key][0] == 5:
        print(key)
        print(big_sto[key])
