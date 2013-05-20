#!/usr/bin/python

import sys

# need to emit at least 1 for every tweet id so that they all end up in the output
def ProcessWord(tweet_list, sentiment_list):
  if len(tweet_list) == 0:
    return

  if len(sentiment_list) > 0:
    value = sentiment_list[0]
  else:
    value = 0

  for t in tweet_list:
    print "{}\t{}".format(t, value)

current_word = None
tweet_list = []
sentiment_list = []

for line in sys.stdin:
  line = line.strip()
  args = line.split('\t')
  word = args[0]
  if word != current_word:
    if current_word:
      ProcessWord(tweet_list, sentiment_list)
    tweet_list = []
    sentiment_list = []
    current_word = word

  if args[1] == "tweet":
    tweet_list.append(args[2])
  elif args[1] == "sentiment":
    sentiment_list.append(int(args[2]))
    assert len(sentiment_list) in [0,1]
  else:
    assert False

if current_word:
  ProcessWord(tweet_list, sentiment_list)
