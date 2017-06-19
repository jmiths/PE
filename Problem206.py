#!/usr/bin/python
'''
for i in range(0,10):
    temp = ""
    for j in range(1,10):
        temp = temp + str(j) + str(i)
    temp = int(temp+"0")
    print temp
    print math.sqrt(temp)
'''

for i in range(1010101010,1389026624):
    temp = str(i**2)
    if temp[0] == "1":
        if temp[2] == "2":
            if temp[4] == "3":
                if temp[6] == "4":
                    if temp[8] == "5":
                        if temp[10] == "6":
                            if temp[12] == "7":
                                if temp[14] == "8":
                                    if temp[16] == "9":
                                        if temp[18] == "0":
                                            print i
                                            print temp
                                            quit()
