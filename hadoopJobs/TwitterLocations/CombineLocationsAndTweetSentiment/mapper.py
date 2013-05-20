#!/usr/bin/python

import sys

for line in sys.stdin:
  line = line.strip()
  args = line.split('\t')
  if len(args) == 6: # tweet/sentiment
    tweetid, text, userid, user_str, sentiment_score, sentiment_score_count = args
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(userid, "tweet", tweetid, text, user_str, sentiment_score, sentiment_score_count,))
  else: # tweeter location
    userid, city, city_score, city_count = args
    print("{}\t{}\t{}\t{}\t{}".format(userid, "location", city, city_score, city_count))
