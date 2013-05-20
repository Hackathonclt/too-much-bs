#!/usr/bin/python

import sys

for line in sys.stdin:
  line = line.strip()
  args = line.split('\t')
  if args[0] == 'tweet':
    user = args[1]
    words = set(args[2].split())
    tweetid = args[3]
    for word in words:
      print("{}\t{}".format(word, tweetid))
  else:
    assert len(args) == 3
    word1, word2 = args[0].split()
    score = args[1]
    count = args[2]
    print("{}\t{}\t{}\t{}".format(word1, word2, score, count))
    print("{}\t{}\t{}\t{}".format(word2, word1, score, count))
