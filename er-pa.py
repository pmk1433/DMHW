from networkx import *
import sys

n = 10 # 10 nodes
m = 8
p = 0.5 # 20 edges

G = erdos_renyi_graph(n,p)

# some properties
print("node degree clustering")
for v in nodes(G):
    print('%s %d %f' % (v,degree(G,v),clustering(G,v)))

# print the adjacency list to terminal
try:
    write_adjlist(G,sys.stdout)
except TypeError: # Python 3.x
    write_adjlist(G,sys.stdout.buffer)


G = barabasi_albert_graph(n, m)

# some properties
print("node degree clustering")
for v in nodes(G):
    print('%s %d %f' % (v,degree(G,v),clustering(G,v)))

# print the adjacency list to terminal
try:
    write_adjlist(G,sys.stdout)
except TypeError: # Python 3.x
    write_adjlist(G,sys.stdout.buffer)
