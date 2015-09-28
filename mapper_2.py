#!/usr/bin/python 
import sys

for line in sys.stdin:
  print line.split("\t")[1].strip() + "\t1"
