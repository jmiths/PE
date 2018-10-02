#!/usr/bin/python3
total = 0
for i in range(1,100):
    for j in range(1,100):
        temp = str(i**j)
        if len(temp) == j:
            total = total + 1
            print (temp +" "+str(j))
print("total: " + str(total))
