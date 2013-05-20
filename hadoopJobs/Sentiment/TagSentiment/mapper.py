#!/usr/bin/python

import sys

for line in sys.stdin:
  line = line.strip()
  print "{}\t{}".format("sentiment", line)
