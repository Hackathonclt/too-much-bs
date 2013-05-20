#!/usr/bin/python

import sys
import json
import string
import re

# replaces all white space
# useful for removing newline, carraige return, tabs in text, etc.
p = re.compile(r'\s+')

for line in sys.stdin:
  line = line.strip()
  tweet = json.loads(line)

  if 'text' in tweet:
    tweet_text = p.sub(' ', tweet['text'].encode('ascii', 'ignore').strip())
    if tweet_text == "":
      continue # possibly if only non-ascii unicode characters
    tweet_id = tweet['id']
    tweeter_id = tweet['user']['id']
    tweeter_handle = p.sub(' ', tweet['user']['screen_name'].strip().encode('ascii', 'ignore'))

    s = u"{}\t{}\t{}\t{}".format(tweet_id, tweet_text, tweeter_id, tweeter_handle)
    print s
