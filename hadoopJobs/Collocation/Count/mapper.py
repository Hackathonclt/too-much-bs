#!/usr/bin/python

import sys
import math

for line in sys.stdin:
  line = line.strip()
  args = line.split('\t')
  text = args[2]
  words = len(set(text.split()))
  if words > 1:
    combs = math.factorial(words)/(2*math.factorial(words-2))
  else:
    combs = 0
  print "key\t{}".format(combs)
