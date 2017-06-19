#!/usr/bin/python

from decimal import *
import re

getcontext().prec=10000

pattern = re.compile(r"([0-9]+?)\1+")

greatest = 0

for i in range(2,1000):
    num = str(Decimal(1) / Decimal(i))
    num = num[2:]
    match = pattern.findall(num)
    for element in match:
        if greatest < len(element):
            greatest = len(element)
            print i
