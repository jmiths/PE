#!/usr/bin/python3

primes = [1]*500000
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

big_len = 22
for i in range(len(p)):
    if p[i] > 150:
        break
    for j in range(big_len+1,len(p)):
        sump = sum(p[i:j])
        if sump > 1000000:
            break
        if sump in p:
            print(p[i],sump,j)
            big_len = j
print(big_len)
