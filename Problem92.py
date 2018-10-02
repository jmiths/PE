#!/usr/bin/python3

big_sto={}
for i in range(1,10000000):
    if i % 100000 == 0:
        print(i)
    prog = [i]
    temp = i
    while not(temp == 1 or temp == 89):
        if temp in big_sto:
            temp = big_sto[temp]
        else:
            prog.append(temp)
            temp = str(temp)
            s = 0
            for char in temp:
                s = s + int(char)**2
            temp = s
    if temp == 1:
        for elem in prog:
            big_sto[elem] = 1
    elif temp == 89:
        for elem in prog:
            big_sto[elem] = 89
print("Dict Done")
total = 0
for key in big_sto:
    if key >= 10000000:
        continue
    if big_sto[key] == 89:
        total = total + 1
print(total)
