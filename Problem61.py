#!/usr/bin/python3
# Solution for https://projecteuler.net/problem=61

# Dictionary with format {First Two Digits : [['Tri','SQ',etc.], Second Two digits]}
all_nums = {}

# Generate all Triangular Number for Four digits (1000 - 9999)
# Code could be condensed for each generation
# (x*(x+1))/2 > 1000
# x*(x+1) > 2000
# x^2 + x > 2000
# x^2 + x - 2000 > 0
# Over at 45

x = 45
n = (x*(x+1))/2
while n < 10000:
    temp = str(int(n))
    if temp[2] == "0":
        x = x + 1
        n = (x*(x+1))/2
        continue
    fh = temp[:2]
    lh = temp[2:]
    if fh not in all_nums:
        all_nums[fh] = [["TRI",lh]]
    else:
        all_nums[fh].append(["TRI",lh])
    x = x + 1
    n = (x*(x+1))/2

# Generate all Square Numbers for Four Digits (1000,9999)
# x^2 > 1000
# x^2 - 1000 > 0
# Over at 32

x = 32
n = x**2
while n < 10000:
    temp = str(int(n))
    if temp[2] == "0":
        x = x + 1
        n = x ** 2
        continue
    fh = temp[:2]
    lh = temp[2:]
    if fh not in all_nums:
        all_nums[fh] = [["SQ",lh]]
    else:
        all_nums[fh].append(["SQ",lh])
    x = x + 1
    n = x ** 2

# Generate all PENT numbers for Four Digits (1000,9999)
# (x(3x-1))/2 > 1000
# x(3x-1) > 2000
# 3x^2 - x > 2000
# 3x^2 - x - 2000 > 0
# Over at 26

x = 26
n = (x*(3*x-1))/2
while n < 10000:
    temp = str(int(n))
    if temp[2] == "0":
        x = x + 1
        n = (x*(3*x-1))/2
        continue
    fh = temp[:2]
    lh = temp[2:]
    if fh not in all_nums:
        all_nums[fh] = [["PENT",lh]]
    else:
        all_nums[fh].append(["PENT",lh])
    x = x + 1
    n = (x*(3*x-1))/2

# Generate all HEXA numbers for Four digits (1000,9999)
# x*(2x-1) > 1000
# 2x^2 - x > 1000
# 2x^2 - x - 1000 > 0
# Over at 23

x = 23
n = x*(2*x-1)
while n < 10000:
    temp = str(int(n))
    if temp[2] == "0":
        x = x + 1
        n = x*(2*x-1)
        continue
    fh = temp[:2]
    lh = temp[2:]
    if fh not in all_nums:
        all_nums[fh] = [["HEXA",lh]]
    else:
        all_nums[fh].append(["HEXA",lh])
    x = x + 1
    n = x*(2*x-1)

# Generate all HEPT numbers for four digits (1000,9999)
# x(5x-3)/2 > 1000
# x(5x-3) > 2000
# 5x^2 - 3x - 2000 > 0
# Over at 21

x = 21
n = (x*(5*x-3))/2
while n < 10000:
    temp = str(int(n))
    if temp[2] == "0":
        x = x + 1
        n = (x*(5*x-3))/2
        continue
    fh = temp[:2]
    lh = temp[2:]
    if fh not in all_nums:
        all_nums[fh] = [["HEPT",lh]]
    else:
        all_nums[fh].append(["HEPT",lh])
    x = x + 1
    n = (x*(5*x-3))/2

# Generate all OCTA numbers for four digits (1000,9999)
# x(3x-2) > 1000
# 3x^2-2x - 1000 > 0
# Over at 19

x = 19
n = x*(3*x-2)
while n < 10000:
    temp = str(int(n))
    if temp[2] == "0":
        x = x + 1
        n = x*(3*x-2)
        continue
    fh = temp[:2]
    lh = temp[2:]
    if fh not in all_nums:
        all_nums[fh] = [["OCTA",lh]]
    else:
        all_nums[fh].append(["OCTA",lh])
    x = x + 1
    n = x*(3*x-2)

# Print the list to see if we got it
for key in all_nums:
    print(key + ": ",end="")
    print(all_nums[key])

#Figure out which bit of the solution string each digit type will give, could enum, but harder to debug
def which_bit(string):
    if string == "TRI":
        return 0
    elif string == "SQ":
        return 1
    elif string == "PENT":
        return 2
    elif string == "HEXA":
        return 3
    elif string == "HEPT":
        return 4
    elif string == "OCTA":
        return 5
    else:
        print("PANIC at: " + string)
        exit

# When we are building the solution string we need to mark which bits we use, so we can decide if we can use the next chain
def mark_a_bit(v,arr):
    arr[which_bit(v[0])] = 1
    return arr

# If we ran out of chains, then we have to regress and build a different way, so we need to unmark the bit of the solution string
def unmark_bit(v,arr):
    arr[which_bit(v[0])] = 0
    return arr

# Can we continue to build chains or revert?
def can_progress(bits,v): # Takes in solution string and prospective chain continuation
    if v[1] not in all_nums or bits[which_bit(v[0])] != 0: # If prospective chain can't continue on after this, then abort early or if the bit we want to change is not zero
        return False
    else:
        return True

# Build the solution string to actual values so that I can read the final solution and then print
def reconstruct(solution): 
    arr = []
    for i in range(len(solution)):
        arr.append(int(solution[i-1][1]+solution[i][1]))
    print(arr)
    print(sum(arr))

for key in all_nums: # Start reading the whole dict
    for v1 in all_nums[key]: # For the values, step one level down and look through the next level
        bits = [0,0,0,0,0,0] #TRI,SQ,PENT,HEXA,HEPT,OCTA # Init solution bitmask
        solution = [v1] # Init solution string
        bits = mark_a_bit(v1,bits) # Mark the first bit with the item I started with
        if v1[1] in all_nums: # Is 1 level down still in the set?
            for v2 in all_nums[v1[1]]: #Use Previous value to find new subset of values
                if can_progress(bits,v2): # Do the first two match or can we continue?
                    solution.append(v2) # Add to solution string
                    bits = mark_a_bit(v2,bits) # Repeat until solved
                    for v3 in all_nums[v2[1]]:
                        if can_progress(bits,v3):
                            solution.append(v3)
                            bits = mark_a_bit(v3,bits)
                            for v4 in all_nums[v3[1]]:
                                if can_progress(bits,v4):
                                    solution.append(v4)
                                    bits = mark_a_bit(v4,bits)
                                    for v5 in all_nums[v4[1]]:
                                        if can_progress(bits,v5):
                                            solution.append(v5)
                                            bits = mark_a_bit(v5,bits)
                                            for v6 in all_nums[v5[1]]:
                                                if can_progress(bits,v6):
                                                    solution.append(v6)
                                                    for v7 in all_nums[v6[1]]:
                                                        if v1 == v7: # If the start and end value is the same then we are finished
                                                            reconstruct(solution) # Print readable solution string
                                                            solution.append(v7)
                                                            print()
                                                            print(solution) # Print order
                                                            solution.pop()
                                                            quit() # I only need one
                                                    solution.pop() # If I failed, regress
                                            bits = unmark_bit(v5,bits) # If failed, regress
                                            solution.pop()
                                    solution.pop() # If failed, regress
                                    bits = unmark_bit(v4,bits)
                            solution.pop()
                            bits = unmark_bit(v3,bits)
                    solution.pop()
                    bits = unmark_bit(v2,bits)
        bits = unmark_bit(v1,bits)
        solution.pop()
