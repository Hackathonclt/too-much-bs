#!/usr/bin/python

import sys

total_count = 0
for line in sys.stdin:
  line = line.strip()
  args = line.split('\t')
  val = int(args[1])
  total_count += val
print "key\t{}".format(total_count)
