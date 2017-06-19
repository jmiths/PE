#!/usr/bin/python

fibs = [1]

fib = 1
score = 0
for i in range(1,101):
    fib *= i
    fibs.append(fib)
for n in range(1,101):
    for r in range(1,n+1):
        if fibs[n] / (fibs[r] * fibs[n-r]) > 1000000:
            score += 1
print score
