from networkx import *
import random
import sys
import pdb;

budget = int(sys.argv[1])

G = read_edgelist(str(sys.argv[2])) # erdos_renyi_graph(num,p)

immunized = set()
remaining = G.copy().nodes()
print "Immunizing ACC"
for i in xrange(budget):
  #print "\n\n\nBefore the removal: " + str(G.nodes()), remaining
  candidate_initial = random.choice(remaining)

  neighbors = []
  for n in all_neighbors(G,candidate_initial):
    if n in remaining:
      neighbors.append(n)
  if len(neighbors) > 0:
    candidate = random.choice(neighbors)

  if candidate in G.nodes(): G.remove_node(candidate)
  if candidate in remaining:     remaining.remove(candidate)
  #print "After the removal: " + str(G.nodes()), remaining
  immunized.add(candidate)

print "Immunized: ", immunized
