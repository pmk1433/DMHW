#!/usr/bin/python
import sys
for line in sys.stdin:
  red = line.split("\t")[1].strip()
  print(red + "\t1")
