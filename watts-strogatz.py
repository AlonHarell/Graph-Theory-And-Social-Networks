import networkx as nx
import numpy as np

def Watts_Strogatz(n,k,p):
    #Phase 1
    G = nx.Graph()
    for i in range(0,n):
        G.add_node(i)
    allnodes = set(G)

    for i in range(0,n):
        for j in range(1,int(k/2)+1): #Connecting each node to k/2 neighbors on each side. Using cycling (mod n).
            G.add_edge(i,(i+j)%n)
            G.add_edge(i,(i-j)%n)

    #Phase 2
    for e in G.edges():
        if (np.random.binomial(1,p) == 1): #Binomial with n=1 is bernoulli.
            u = e[0]
            neighbors = set(G.neighbors(u))
            neighbors.add(u)
            v = np.random.choice(list(allnodes - neighbors)) #On probability p, remove edge and add a random one between node and non-neighbors
            G.remove_edge(e[0],e[1])
            G.add_edge(u,v)

    return G
