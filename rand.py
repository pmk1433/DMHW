from networkx import *
import random
import sys
import pdb;

budget = int(sys.argv[1])

G = read_edgelist(str(sys.argv[2]))

immunized = set()
remaining = G.copy().nodes()
print "Immunizing RAND"
for i in xrange(budget):
  candidate = random.choice(remaining)

  if candidate in G.nodes(): G.remove_node(candidate)
  if candidate in remaining:     remaining.remove(candidate)
  immunized.add(candidate)

print "Immunized: ", immunized
