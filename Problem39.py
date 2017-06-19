#!/usr/bin/python
import math
# num.is_integer()

perms = {}

for hypot in range(1,1000):
	hypot_sq = hypot**2
	for adjacent in range(1,int(hypot/2)+1):
		adj_sq = adjacent**2 + .0
		opposite = math.sqrt(hypot_sq - adj_sq)
		perminter = hypot + adjacent + opposite
		if opposite != 0 and opposite.is_integer() and hypot + adjacent + opposite <= 1000:
			if perminter in perms:
				perms[perminter] += 1
			else:
				perms[perminter] = 1

best = 0
num = 0

for key in perms:
	if perms[key] > num:
		num = perms[key]
		best = key

print "best:" + str(best) + " num: " + str(num)
