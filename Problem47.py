#!/usr/bin/python

import subprocess

blah = subprocess.check_output(["factor",str(14)])
blah = blah.strip().split(" ")
print blah
