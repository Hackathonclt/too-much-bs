#!/usr/bin/python

import sys

for line in sys.stdin:
  line = line.strip()
  (name, city) = line.split('\t', 1)
  print "{}\t{}\t{}".format("venue", name, city)

