#!/usr/bin/python

# see README for big idea
#
# MAPPER
# parse out city and name

import sys
import string
for line in sys.stdin:
  line = line.strip()
  args=line.split("\t")
  if len(args) != 5:
    continue
  city = args[0].strip()
  name = args[2].strip()
  # change name to "cononical form" -- all lowercase, no puncuation
  name = name.translate(string.maketrans("",""), string.punctuation).strip().lower()
  if name == "":
    continue
  
  # forget about others
  print "{}\t{}".format(name, city)
