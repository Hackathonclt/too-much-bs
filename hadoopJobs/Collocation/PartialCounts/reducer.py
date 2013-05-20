#!/usr/bin/python

import sys
import collections

# process a word group
# the key is word A
# word B is a dictionary of other words that are paired with A
# mapped to the count of (A,B) frequency
def ProcessWordBin(word_A, word_B_frequency):
  # word A frequency is the sum of word_B_frequency
  A_frequency = sum(word_B_frequency.values())
  for word_B, frequency in word_B_frequency.items():
    (sortA, sortB) = sorted( (word_A, word_B) )
    print "{} {}\t{}\t{}\t{}".format(sortA, sortB, word_A, frequency, A_frequency)

current_word = None
word_key = None

for line in sys.stdin:
  line = line.strip()
  (word_key, word_B, frequency) = line.split('\t')
  if word_key != current_word:
    if current_word:
      ProcessWordBin(current_word, word_B_frequency)
    word_B_frequency = collections.defaultdict(int)
    current_word = word_key

  word_B_frequency[word_B] += int(frequency)

if current_word:
  ProcessWordBin(current_word, word_B_frequency)
