#!/usr/bin/python

import sys
file_name = sys.argv[1]
city = sys.argv[2]

fin = open(file_name)
fout = open(city + '.out', 'w')

for line in fin:
  fout.write("{}\t{}".format(city, line))
fin.close()
fout.close()
