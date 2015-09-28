#!/usr/bin/python
import sys

count = 0
current = None
for line in sys.stdin:
  number = line.split("\t")[0].strip()
  if current == number:
    count += 1
  else:
    if current:
      print current + "\t" + str(count)
    count = 1
    current = number
