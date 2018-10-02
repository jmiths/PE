#!/usr/bin/python3

a=[ [131, 673, 234, 103, 18 ],
    [201,  96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524,  37, 331] ]
print(a)

pyr=[]
for y in range(len(a)):
    row = []
    for x in range(1,len(a)+2):
        for z in range(0,x):
            row.append(a[z+(x-1)][(x-1)-z])
print(pyr)
