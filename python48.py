#!/usr/bin/python3
primes = [1]*3000
primes[0] = 0
p = [2]

for index in range(len(primes)):
    if primes[index] == 0:
        continue
    else:
        for bad_val in range(index*(2+(2*index)),len(primes),2*index+1):
            primes[bad_val] = 0

for index in range(len(primes)):
    if primes[index] == 1:
        p.append(2*index+1)
#print(p)

arr = [i for i in range(2,1000000)]
temp = ''
for num in arr:
    s = set()
    #if num in p:
    #    temp += '0'
    #    continue
    for prime in p:
        if num == 0 or prime > num:
            break
        while num % prime == 0:
            s.add(prime)
            num = int(num/prime)
    temp += (str(len(s)))
print(temp.index("4444")+2)
