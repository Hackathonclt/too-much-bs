#!/usr/bin/python

import sys
import re
p=re.compile('.*[0-9]')

support_threshold = 70
ratio_threshold = 600

for line in sys.stdin:
  line = line.strip()
  (pair, ratio, support) = line.split('\t')
  word1, word2 = pair.split()
  support = int(support)
  ratio = float(ratio)
  if support >= support_threshold and ratio >= ratio_threshold and len(word1) > 3 and len(word2) > 3 and not p.match(word1) and not p.match(word2): # change threshold here!
    print line
