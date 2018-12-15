#!/usr/bin/python3
import re
#a = [[ 7, 53, 183, 439, 863], [497, 383, 563,  79, 973], [287,  63, 343, 169, 583], [627, 343, 773, 959, 943], [767, 473, 103, 699, 303]]
a = []
with open("p345.txt") as f:
   for line in f:
      line = line.split()
      line = list(map(int, line))
      a.append(line)

class locs:
   def __init__(self,val,x,y):
      self.val = val
      self.x = x
      self.y = y
   def __repr__(self):
      return str(self.val)

def make_largest(lis,n,s,x,y):
   if n == 15:
      print(s)
      return
   for ele in lis:
      if x[ele.x] == 0 and y[ele.y] == 0:
         x[ele.x] = 1
         y[ele.y] = 1
         make_largest(lis[1:],n+1,s+ele.val,x,y)
         x[ele.x] = 0
         y[ele.y] = 0
eles = []
for y in range(len(a)):
   for x in range(len(a[y])):
      eles.append(locs(a[y][x],x,y))
#print(eles)
eles = sorted(eles,key=lambda loc:loc.val)[::-1]

make_largest(eles,0,0,[0]*20,[0]*20)
