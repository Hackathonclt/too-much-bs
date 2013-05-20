#!/usr/bin/python

import sys

current_id = None
total_score = 0
count = 0
for line in sys.stdin:
  line = line.strip()
  (tweetid, score) = line.split('\t')
  score = int(score)
  if current_id != tweetid:
    if current_id:
      print "{}\t{}\t{}".format(tweetid, total_score, count)
    current_id = tweetid
    total_score = 0
    count = 0
  total_score += score
  if score != 0:
    count += 1

if current_id:
  print "{}\t{}\t{}".format(tweetid, total_score, count)
