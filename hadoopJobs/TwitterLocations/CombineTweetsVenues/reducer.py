#!/usr/bin/python

import sys

# prints out (twitter user id, city) for each match between venue and a tweet
def ProcessWord(venues_set, tweet_set):
  if len(venues_set) == 0 or len(tweet_set) == 0:
    return
  for venue_name, city in venues_set:
    for user, text in tweet_set:
      if venue_name in text:
        print "{}\t{}".format(user, city)


current_word = None
word = None
venues_set = []
tweet_set = []
for line in sys.stdin:
  line = line.strip()
  args = line.split('\t')
  word = args[0]

  if word != current_word:
    if current_word:
      # process current_word
      ProcessWord(venues_set, tweet_set)

    venues_set = []
    tweet_set = []
    current_word = word

  # process a line
  line_type = args[1]
  if line_type == "tweet":
    user = args[2]
    text = args[3]
    tweet_set.append( (user, text,) )
  elif line_type == "venue":
    venue_name = args[2]
    city = args[3]
    venues_set.append( (venue_name, city,) )

if current_word:
  ProcessWord(venues_set, tweet_set)
