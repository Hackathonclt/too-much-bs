#!/usr/bin/python

import sys

current_tweet = None

for line in sys.stdin:
  line = line.strip()
  args = line.split('\t')
  tweetid = args[0]
  if tweetid != current_tweet:
    if current_tweet:
      if not have_tweet:
        continue
      if not have_score:
        score = 0
        count = 0
      print("{}\t{}\t{}\t{}\t{}\t{}".format(tweetid, text, user, user_str, score, count))
    current_tweet = tweetid
    have_score = False
    have_tweet = False

  if args[1] == 'tweet':
    have_tweet = True
    try:
      if len(args) == 5:
        text, user, user_str = args[2:]
      else:
        text, user = args[2:]
        user_str = "None"
    except:
      sys.stderr.write("{}\n".format(args))
      raise
  elif args[1] == 'sentiment':
    have_score = True
    try:
      score, count = args[2:]
    except:
      sys.stderr.write("{}\n".format(args))
      raise
  else:
    assert False
