from networkx import *
import random
import sys
import pdb;

n = 37 # 10 nodes

p = 0.5 # 20 edges

budget = 10

# Generating the ER graph
G_er = erdos_renyi_graph(n,p)

# some properties
print("node degree clustering")
for v in nodes(G_er):
   print('%s %d %f' % (v,degree(G_er,v),clustering(G_er,v)))

write_adjlist(G_er, sys.stdout)

G_pl = barabasi_albert_graph(n, 1)

# some properties
print("node degree clustering")
for v in nodes(G_pl):
   print('%s %d %f' % (v,degree(G_pl,v),clustering(G_pl,v)))

write_adjlist(G_pl, sys.stdout)


  
  
    


    
      
     


  


