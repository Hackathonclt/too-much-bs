#!/usr/bin/python

import sys
import re
p = re.compile('.*[0-9]')

# each word now associated with this tweet
def ProcessTweet(twitterid, words):
  for word in words.keys():
    max_score = 0
    total_count = 0
    for score, count in words[word]:
      max_score = max(max_score, score)
      total_count += count
    print("{}\t{}\t{}\t{}".format(word, twitterid, max_score, total_count))

import collections
words = collections.defaultdict(list)

current_tweet = None

for line in sys.stdin:
  line = line.strip()
  tweet, word, score, count = line.split('\t')
  score = float(score)
  count = int(count)

  if tweet != current_tweet:
    if current_tweet:
      ProcessTweet(tweet, words)
    current_tweet = tweet
    words = collections.defaultdict(list)

  words[word].append( (score, count,) )

if current_tweet:
  ProcessTweet(tweet, words)
