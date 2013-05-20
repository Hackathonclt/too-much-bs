#!/usr/bin/python

# no op
import re
p = re.compile('.*[0-9]')
import sys

for line in sys.stdin:
  line = line.strip()
  tweet, word, score, count = line.split('\t')
  if len(word) > 3 and not p.match(word):
    print line
