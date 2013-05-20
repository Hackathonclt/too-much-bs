#!/usr/bin/python

import sys
import math

# take pairs of (A,B) word collocation info and produce LLC

total_pair_count = 411127046

# shannon entropy
def H(elements):
  s = 0.0;
  for element in elements:
    s += element
  ret = 0.0
  for element in elements:
    assert element >= 0.0
    zero_flag = element == 0
    ret += element * math.log( (element + zero_flag) / s)
  return -ret

def LLR(k11, k12, k21, k22):
  row_entropy = H( (k11, k12,) ) + H( (k21, k22,) )
  column_entropy = H( (k11, k21,) ) + H( (k12, k22,) )
  matrix_entropy = H( (k11, k12, k21, k22,) )
  return 2*(matrix_entropy - row_entropy - column_entropy)

def ProcessPair(total_pair_count, word_A, word_B, A_frequency, B_frequency, pair_frequency):
  k11 = pair_frequency
  k21 = A_frequency - pair_frequency
  k12 = B_frequency - pair_frequency
  k22 = total_pair_count - (A_frequency + B_frequency - pair_frequency)
  ratio = LLR(k11, k12, k21, k22)

  if word_A < word_B:
    first_word = word_A
    second_word = word_B
  else:
    first_word = word_B
    second_word = word_A
  # store the pair, LLR, and support (pair_frequency)
  print "{} {}\t{}\t{}".format(first_word, second_word, ratio, pair_frequency)

current_pair = None
pair = None
pair_count = 0
for line in sys.stdin:
  line = line.strip()
  (pair, word, pair_frequency, word_frequency,) = line.split('\t')
  pair_frequency = int(pair_frequency)
  word_frequency = int(word_frequency)

  if pair != current_pair:
    if current_pair:
      assert pair_count == 2
      ProcessPair(total_pair_count, word_A, word_B, word_A_frequency, word_B_frequency, word_A_pair_frequency)
    current_pair = pair
    pair_count = 0

  if pair_count == 0:
    word_A = word
    word_A_frequency = word_frequency
    word_A_pair_frequency = pair_frequency
  elif pair_count == 1:
    word_B = word
    word_B_frequency = word_frequency
    assert(word_A_pair_frequency == pair_frequency)
  elif pair_count == 2:
    assert pair != current_pair

  pair_count += 1

if current_pair:
  assert pair_count == 2
  ProcessPair(total_pair_count, word_A, word_B, word_A_frequency, word_B_frequency, word_A_pair_frequency)
