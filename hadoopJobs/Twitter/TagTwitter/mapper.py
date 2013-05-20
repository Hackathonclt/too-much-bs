#!/usr/bin/python

import sys
import string
import re

# need to recompress whitespace since multiple white spaces may be created after removing punctuation
p = re.compile(r'\s+')

for line in sys.stdin:
  line = line.strip()
  args = line.split('\t')
  tweetid = args[0]
  text = args[1]
  user = args[2]

  # make text canonical
  text = p.sub(' ', text.translate(string.maketrans("",""), string.punctuation).strip().lower())
  if text == "":
    continue

  print "{}\t{}\t{}\t{}".format('tweet', user, text, tweetid)
