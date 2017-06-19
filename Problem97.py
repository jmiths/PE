#!/usr/bin/python

#28433*(2**7830457)+1

tot = 2
for i in range(1,7830457):
    if tot > 1000000000000:
        tot %= 10000000000
    tot *= 2
tot *= 28433

tot += 1

print tot
