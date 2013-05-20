#!/usr/bin/python

import sys
import re
import string
p = re.compile(r'\s+') # get rid of spaces after removing punctuation

for line in sys.stdin:
  line = line.strip()
  args = line.split('\t')
  if len(args) in [3,4]: # tweet
    tweetid = args[0]
    text = args[1]
    text = p.sub(' ', text.translate(string.maketrans("",""), string.punctuation).strip().lower())
    words = set(text.split())
    for word in words:
      print "{}\t{}\t{}".format(word, "tweet", tweetid)
  elif len(args) == 2: # sentiment
    word = args[0]
    value = args[1]
    print "{}\t{}\t{}".format(word, "sentiment", value)
  else:
    sys.stderr.write("{}\n".format(line))
    assert False
