#!/usr/bin/python

import sys
import re
import string

p = re.compile(r'\s+')

for line in sys.stdin:
  line = line.strip()
  args = line.split('\t')
  if args[0] == "sentiment":
    try:
      tweetid, score, count = args[1:]
    except:
      sys.stderr.write("{}\n".format(args))
      raise
    print "{}\t{}\t{}\t{}".format(tweetid, "sentiment", score, count)
  else: # tweet
    try:
      tweetid, text, user = args[0:3]
    except:
      sys.stderr.write("{}\n".format(args))
      raise
    #text = p.sub(' ', text.translate(string.maketrans("",""), string.punctuation).strip().lower())
    if len(args) > 3:
      user_str = args[3]
    else:
      user_str = ""
    print "{}\t{}\t{}\t{}\t{}".format(tweetid, "tweet", text, user, user_str)
