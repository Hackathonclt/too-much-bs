#!/usr/bin/python

import sys

for line in sys.stdin:
  line = line.strip()
  args = line.split('\t')
  text = args[2]
  words = sorted(set(text.split()))
  for i in range(len(words)):
    for j in range(i+1, len(words)):
      A = words[i]
      B = words[j]
      print "{}\t{}\t{}".format(A, B, 1)
      print "{}\t{}\t{}".format(B, A, 1)
