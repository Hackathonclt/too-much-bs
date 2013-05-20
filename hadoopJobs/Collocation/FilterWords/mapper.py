#!/usr/bin/python

import sys
import re
p = re.compile('.*[0-9]')
for line in sys.stdin:
  line = line.strip()
  args = line.split('\t')
  word1, word2 = args[0].split()
  if len(word1) < 4 or len(word2) < 4 or p.match(word1) or p.match(word2):
    continue
  print line
