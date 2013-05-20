#!/usr/bin/python

import sys

max_score = 291282.79 + 1
max_count = 287738 + 1

# each tweet should now be associated with the search words
# also include the actual word with max count and score
def ProcessWordBin(word, tweets, search_words):
  if len(tweets) == 0:
    return
  # generate bin word
  for t in tweets:
    print "{}\t{}\t{}\t{}".format(t, word, max_score, max_count)
    for w in search_words:
      print "{}\t{}\t{}\t{}".format(t, w[0], w[1], w[2])

current_word = None
word = None
tweets = []
search_words = []

for line in sys.stdin:
  line = line.strip()
  args = line.split('\t')
  word = args[0]

  if current_word != word:
    if current_word:
      ProcessWordBin(current_word, tweets, search_words)
    current_word = word
    tweets = []
    search_words = []

  if len(args) == 2: # tweet
    tweetid = args[1]
    tweets.append(tweetid)
  else:
    assert len(args) == 4 # search word
    search_word, score, count = args[1:]
    search_words.append( (search_word, score, count,) )

if current_word:
  ProcessWordBin(current_word, tweets, search_words)
