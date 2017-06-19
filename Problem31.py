#!/usr/bin/python

# Courtesy of Greg Kilmer

goal = 200
coins = [1,2,5,10,20,50,100,200]
options = []

for i in range(goal+1):
    options.append(0)

options[0] = 1  

# After first iteration of the first coin, there is 1 way to find it

for coin in coins:
    for i in range(coin,goal+1):
        options[i] += options[i - coin] # Adds last bucket

print options[goal] 
