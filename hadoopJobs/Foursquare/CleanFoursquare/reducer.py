#!/usr/bin/python
# see README for big idea

# REDUCER
# take (name, city) pairs and procude (name, set(cities))

def ProcessVenue(venue, city_set):
  s = venue
  for city in city_set:
    s += "\t{}".format(city)
  print s

import sys
current_key = None
name = None
cities = set()
for line in sys.stdin:
  line = line.strip()
  name, city = line.split('\t', 1)

  if name != current_key:
    if current_key:
      ProcessVenue(current_key, cities)
    # start new key (name)
    current_key = name
    cities = set()

  cities.add(city)

# last name
if current_key:
  ProcessVenue(name, cities)
