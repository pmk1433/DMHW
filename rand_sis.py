from networkx import *
import random
import sys
import pdb;

num = 100 # 100 nodes

p = 0.25 # 25% probability

budget = 10

b = 0.2
g = 0.2
max_time = 500

G = erdos_renyi_graph(num,p)

immunized = set()
remaining = G.copy().nodes()
print "Immunizing RAND"
for i in xrange(budget):
  candidate = random.choice(remaining)

  if candidate in G.nodes(): G.remove_node(candidate)
  if candidate in remaining:     remaining.remove(candidate)
  immunized.add(candidate)

print "Immunized: ", immunized

print "Done RAND", "\nRAND Done"

N = G.nodes()
status_list = [True] * num # Initally all nodes are considered infected.

for imm in immunized:
  status_list[imm] = 'IMMUNE' # Immunized nodes cannot become infected

with open("rand_sis_results.csv","w+") as f:
  for i in xrange(max_time):
    cnt1 = 0
    cnt2 = 0 
    print "Iteration " + str(i)
    for node in N:

      # For infected nodes, recover with
      # probability gamma
      if status_list[node] == True:
        if random.random() <= g:
          status_list[node] = False

      # For healthy nodes, get infected by each infected 
      # neighbor with probability b
      elif status_list[node] == False:
        for neighbor in all_neighbors(G,node):
          if random.random() <= b:
            status_list[node] = True
      else:
        print "Node is IMMUNIZED"

    for status in status_list:
      if status == True:
        cnt1 += 1
      else:
        cnt2 += 1
    print "No. of Infected nodes: ", cnt1
    print "No. of healthy nodes: ", cnt2
    f.write(str(i+1) + "," + str(cnt1) + "," + str(cnt2) + "\n")
  
print status_list
