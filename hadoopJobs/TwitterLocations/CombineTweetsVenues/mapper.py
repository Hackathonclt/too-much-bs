#!/usr/bin/python

import sys

for line in sys.stdin:
  line = line.strip()
  args = line.split('\t')
  if args[0] == 'tweet':
    user = args[1]
    text = args[2]
    words = set(text.split())
    for word in words:
      print "{}\t{}\t{}\t{}".format(word, 'tweet', user, text)
  if args[0] == 'venue':
    name = args[1]
    city = args[2]
    first_word = name.split()[0]
    print "{}\t{}\t{}\t{}".format(first_word, 'venue', name, city)
