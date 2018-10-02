#!/usr/bin/python

a=[ [131, 673, 234, 103, 18 ],
    [201,  96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524,  37, 331] ]
print(a)

class node:
    def __init__(self,number,weight):
        self.number=number
        self.weight = weight
    def __repr__(self):
        return "I am number: " + str(self.number) + " My value is: " + str(self.weight)
    def number(self):
        return self.number
    def weight(self):
        return self.value

class link:
    def __init__(self,node1,node2,weight):
        self.node1=node1
        self.node2=node2
        self.weight=weight
    def __repr__(self):
        return "I link: " + str(self.node1.number) + " and " + str(self.node2.number) + " My weight is: " + str(self.weight)
    def weight(self):
        return self.weight

list_of_nodes=[]
list_of_links=[]

for y in range(len(a)):
    for x in range(len(a[y])):
        number = (x) + (y*5)
        list_of_nodes.append(node(number,a[y][x]))

for y in range(len(a)):
    for x in range(len(a[y])):
        inode = list_of_nodes[x+(y*5)]
        print(x)
        if x+1 != len(a[y]):
            ilink = list_of_nodes[x+1+(y*5)]
            list_of_links.append(link(inode,ilink,ilink.weight))
        if y+1 != len(a):
            ilink = list_of_nodes[x+((y+1)*5)]
            list_of_links.append(link(inode,ilink,ilink.weight))

for i in list_of_links:
    print(i)
list_of_links = sorted(list_of_links,key=lambda link:link.weight)
print("Now sorted")
for i in list_of_links:
    print(i)
finished_links = [] # [nodes in linked],[links]
#for i in list_of_links:
#    if len(finished_links) == 0:
#        finished_links.append([i.node1,i.node2],i)
#    else:

