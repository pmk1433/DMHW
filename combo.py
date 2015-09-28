from networkx import *
import random
import sys
import pdb;

n = 100 # 100 nodes

p = 0.25 # 25% probability

budget = 10

G = erdos_renyi_graph(n,p)

# some properties
# print("node degree clustering")
# for v in nodes(G):
#    print('%s %d %f' % (v,degree(G,v),clustering(G,v)))

N = G.nodes()

print N
g_acc = G.copy()
g_rand = G.copy()

immunized = set()
remaining = N
print "Immunizing RAND"
for i in xrange(budget):
  candidate = random.choice(remaining)

  if candidate in g_rand.nodes(): g_rand.remove_node(candidate)
  if candidate in remaining:     remaining.remove(candidate)
  immunized.add(candidate)

print "Immunized: ", immunized

print "Done RAND", "\nRAND Done"

immunized = set()
remaining = g_acc.nodes()
print "Immunizing ACC"
for i in xrange(budget):
  #print "\n\n\nBefore the removal: " + str(g_acc.nodes()), remaining
  candidate_initial = random.choice(remaining)

  neighbors = []
  for n in all_neighbors(g_acc,candidate_initial):
    if n in remaining:
      neighbors.append(n)
  if len(neighbors) > 0:
    candidate = random.choice(neighbors)

  #print "\nImmediate before the removal: " + str(g_acc.nodes()), remaining
  #print "\nRemoving: " + str(candidate)
  if candidate in g_acc.nodes(): g_acc.remove_node(candidate)
  if candidate in remaining:     remaining.remove(candidate)
  #print "After the removal: " + str(g_acc.nodes()), remaining
  immunized.add(candidate)

print "Immunized: ", immunized
