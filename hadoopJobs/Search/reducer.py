#!/usr/bin/python

import sys

def ProcessTweet(tweet_id, tweets, words):
  assert len(tweets) in [0,1]
  assert len(words) in [0,1]
  if len(tweets) > 0 and len(words) > 0:
    tweets = tweets[0]
    words = words[0]
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(tweet_id, tweets[0], tweets[1], tweets[2], tweets[3], tweets[4], tweets[5], tweets[6], tweets[7], words[0], words[1]))

current_id = None
tweets = []
words = []

for line in sys.stdin:
  line = line.strip()
  args = line.split('\t')
  twitterid = args[0]
  if twitterid != current_id:
    if current_id:
      ProcessTweet(current_id, tweets, words)
    current_id = twitterid
    tweets = []
    words = []

  if args[1] == 'search_word':
    score,count = args[2:]
    words.append( (score,count,) )
  elif args[1] == 'tweet':
    text, userid, username, sentiment, sentiment_count, city, city_score, city_count = args[2:]
    tweets.append( (text, userid, username, sentiment, sentiment_count, city, city_score, city_count,) )
  else:
    assert False, "line: {}".format(args)

if current_id:
  ProcessTweet(current_id, tweets, words)
