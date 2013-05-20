#!/usr/bin/python

# see README for big idea
#
# MAPPER

import sys
for line in sys.stdin:
  # this time our locations are already in canonical form
  line=line.strip()
  args = line.split("\t")
  if line == "" or len(args) > 2: # implies more than 1 city
    continue
  print line
