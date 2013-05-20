#!/usr/bin/python

query = {
  "search_term"                 : 'grocery'    ,
  "search_term_score"           : 500,
  "search_term_score_dir"       : 1,
  "search_term_count"           : 0,
  "city"                        : 'Charlotte'  ,
  "city_score"                  : .66          ,
  "city_score_dir"              : 1            ,
  "city_count"                  : 5            ,
  "sentiment_score"             : None         ,
  "sentiment_score_dir"         : 1            ,
  "sentiment_count"             : 0            ,
}


import sys

for line in sys.stdin:
  line = line.strip()
  args = line.split('\t')
  if len(args) == 4: # word table
    (word, tweetid, score, count) = args
    score = float(score)
    count = int(count)
    use = True
    if 'search_term' in query:
      use = use and query['search_term'] == word
    if 'search_term_score' in query:
      direction = query['search_term_score_dir']
      if direction >= 0:
        use = use and score >= query['search_term_score']
      else:
        use = use and score <= query['search_term_score']
      if 'search_term_count' in query:
        use = use and count >= query['search_term_count']
    if use:
      print("{}\t{}\t{}\t{}".format(tweetid, 'search_word', score, count))

  elif len(args) == 9: # twitter table
    (tweetid, text, userid, username, sentiment, sentiment_count, city, city_score, city_count) = args
    sentiment = int(sentiment)
    sentiment_count = int(sentiment_count)
    city_score = float(city_score)
    city_count = int(city_count)
    use = True
    if 'city' in query:
      use = use and query['city'] == city
    if 'city_score' in query:
      direction = query['city_score_dir']
      if direction >= 0:
        use = use and city_score >= query['city_score']
      else:
        use = use and city_score <= query['city_score']
      if 'city_count' in query:
        use = use and city_count >= query['city_count']
    if 'sentiment_score' in query:
      direction = query['sentiment_score_dir']
      if direction >= 0:
        use = use and city_score >= query['sentiment_score']
      else:
        use = use and city_score <= query['sentiment_score']
      if 'sentiment_count' in query:
        use = use and city_count >= query['sentiment_count']
    if use:
      print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(tweetid, 'tweet', text, userid, username, sentiment, sentiment_count, city, city_score, city_count))
  else:
    sys.stderr.write("wrong args: {}".format(args))
    assert False
