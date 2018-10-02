#!/usr/bin/python3

all_nums = {}

# TRI
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

# SQ
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

# PENT
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

# HEXA
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

# HEPT
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

#OCTA
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

for key in all_nums:
    print(key + ": ",end="")
    print(all_nums[key])

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

def mark_a_bit(v,arr):
    arr[which_bit(v[0])] = 1
    return arr

def unmark_bit(v,arr):
    arr[which_bit(v[0])] = 0
    return arr

def can_progress(bits,v):
    if v[1] not in all_nums or bits[which_bit(v[0])] != 0:
        return False
    else:
        return True

# Write iterative, recur is hard
#def recur(solution,bits,nex):
#    if len(solution) == 6:
#        return solution
#    elif nex in all_nums:
#        for value in all_nums[nex]:
#            if can_progress(bits,value[0]):
#                solution.append(value)
#                return recur(solution,mark_a_bit(value[0],bits),value[1])

def reconstruct(solution):
    arr = []
    for i in range(len(solution)):
        arr.append(int(solution[i-1][1]+solution[i][1]))
    print(arr)
    print(sum(arr))

for key in all_nums:
    for v1 in all_nums[key]:
        bits = [0,0,0,0,0,0] #TRI,SQ,PENT,HEXA,HEPT,OCTA
        solution = [v1]
        bits = mark_a_bit(v1,bits)
        if v1[1] in all_nums:
            for v2 in all_nums[v1[1]]:
                if can_progress(bits,v2):
                    solution.append(v2)
                    bits = mark_a_bit(v2,bits)
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
                                                        if v1 == v7:
                                                            reconstruct(solution)
                                                            solution.append(v7)
                                                            print()
                                                            print(solution)
                                                            solution.pop()
                                                            quit()
                                                    solution.pop()
                                            bits = unmark_bit(v5,bits)
                                            solution.pop()
                                    solution.pop()
                                    bits = unmark_bit(v4,bits)
                            solution.pop()
                            bits = unmark_bit(v3,bits)
                    solution.pop()
                    bits = unmark_bit(v2,bits)
        bits = unmark_bit(v1,bits)
        solution.pop()
