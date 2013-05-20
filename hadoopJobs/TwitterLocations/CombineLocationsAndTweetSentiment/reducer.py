#!/usr/bin/python

import sys

def ProcessTweetsLocations(user, tweets, locations):
  if len(locations) == 0:
    city = 'None'
    score = 0
    count = 0
  elif len(locations) == 1:
    city = locations[0][0]
    score = locations[0][1]
    count = locations[0][2]
  else:
    assert False, str(locations)

  for tweet in tweets:
    tweetid, text, user_str, sentiment_score, sentiment_score_count = tweet
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(tweetid, text, user, user_str, sentiment_score, sentiment_score_count, city, score, count))

current_user = None

for line in sys.stdin:
  line = line.strip()
  args = line.split('\t')
  userid = args[0]
  if userid != current_user:
    if current_user:
      ProcessTweetsLocations(current_user, tweets, locations)
    current_user = userid
    tweets = []
    locations = []
  if args[1] == 'tweet':
    assert len(args) == 7
    tweets.append(tuple(args[2:]))
  elif args[1] == 'location':
    assert len(args) == 5
    locations.append(tuple(args[2:]))
  else:
    assert False, str(args)

if current_user:
  ProcessTweetsLocations(current_user, tweets, locations)
