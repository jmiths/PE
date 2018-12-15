#!/usr/bin/python3

six = {}
six_tot = 0

for a in range(1,7):
   for b in range(1,7):
      for c in range(1,7):
         for d in range(1,7):
            for e in range(1,7):
               for f in range(1,7):
                  tot = a+b+c+d+e+f
                  six_tot += 1
                  if tot in six:
                     six[tot] = six[tot]+1
                  else:
                     six[tot] = 1
for key in six:
   six[key] = six[key]/six_tot
print(six)

four = {}
four_tot = 0

for a in range(1,5):
   for b in range(1,5):
      for c in range(1,5):
         for d in range(1,5):
            for e in range(1,5):
               for f in range(1,5):
                  for g in range(1,5):
                     for h in range(1,5):
                        for i in range(1,5):
                           tot = a+b+c+d+e+f+g+h+i
                           four_tot += 1
                           if tot in four:
                              four[tot] = four[tot]+1
                           else:
                              four[tot] = 1
for key in four:
   four[key] = four[key]/four_tot
print(four)

six_keys = six.keys()
total_wins = 0
for key in four:
   key_wins = 0
   for versus in six_keys:
      if key > versus:
         key_wins += six[versus]
   total_wins = total_wins + four[key]*key_wins
print(total_wins)
