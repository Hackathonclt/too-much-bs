#!/usr/bin/python

import sys
import collections

# figure out if this user lives in a city
def ProcessUser(user, city_list):
  count = 0
  city_count = collections.defaultdict(int)
  for city in city_list:
    count += 1
    city_count[city] += 1

  # find the mode city
  max_count = 0
  max_city = None

  for k,v in city_count.items():
    if v > max_count:
      max_count = v
      max_city = city

  # store the ratio and support (count)
  # condition for "lives in"
  if max_count > 0:
    print "{}\t{}\t{}\t{}".format(user, city, float(max_count)/float(count), count)

current_key = None
user = None
city_list = []
for line in sys.stdin:
  line = line.strip()
  (user, city) = line.split('\t')
  if user != current_key:
    if current_key:
      ProcessUser(current_key, city_list)
    city_list = []
    current_key = user

  city_list.append(city)

if current_key:
  ProcessUser(user, city_list)
    
