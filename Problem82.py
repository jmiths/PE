#!/usr/bin/python3
'''
a=[ [131, 673, 234, 103, 18 ],
    [201,  96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524,  37, 331] ]
print(a)
'''
#'''
a = []
with open("p081_matrix.txt","r") as f:
        for line in f:
                line = line.strip().split(",")
                line = list(map(int, line))
                a.append(line)
#'''
for y in range(len(a)):
    for x in range(len(a[y])):
        if x == 0 and y == 0:
                continue
        if x == 0:
                m = a[y-1][x]
        elif y == 0:
                m = a[y][x-1]
        else:
                m = min(a[y][x-1],a[y-1][x])
        a[y][x] = a[y][x] + m
l = len(a)
print(a[l-1][l-1])

