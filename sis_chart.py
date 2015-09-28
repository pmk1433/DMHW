from networkx import *
import random
import sys
import pdb;


p = 0.5 # 25% probability


b = 0.2
g = 0.2
max_time = 500

G = barabasi_albert_graph(100, 1)

# some properties
# print("node degree clustering")
# for v in nodes(G):
#    print('%s %d %f' % (v,degree(G,v),clustering(G,v)))

N = G.nodes()
print N

status_dict = {}

for nodecode in N:
  status_dict[nodecode] = True
  

with open("sis_results.csv","w+") as f:
  for i in xrange(max_time):
    cnt1 = 0
    cnt2 = 0 
    print "Iteration " + str(i)
    for node in N:

      # For infected nodes, recover with
      # probability gamma
      if status_dict[node]:
        if random.random() <= g:
          status_dict[node] = False

      # For healthy nodes, get infected by each infected 
      # neighbor with probability b
      else:
        for neighbor in all_neighbors(G,node):
          if random.random() <= b:
            status_dict[node] = True

    for status in status_dict.keys():
      if status_dict[status] == True:
        cnt1 += 1
      else:
        cnt2 += 1
    print "No. of Infected nodes: ", cnt1
    print "No. of healthy nodes: ", cnt2
    f.write(str(i+1) + "," + str(cnt1) + "," + str(cnt2) + "\n")
  
print status_dict


    
      
     


  


