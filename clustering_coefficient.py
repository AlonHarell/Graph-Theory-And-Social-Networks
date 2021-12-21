cimport networkx as nx
import numpy as np

def clustering_coef(G):
    triangles = dict()
    for e in list(G.edges()): #Iterating over edges
        u = e[0]
        v = e[1]
        neighbors_u = G[u]
        neighbors_v = G[v]
        for w in neighbors_u:
            if (w in neighbors_v): #for each common neighbor w, a triangle exists for nodes u,v  (w,u,v)
                triangles[u] = triangles.get(u, 0) + 1
                triangles[v] = triangles.get(v, 0) + 1

    C = 0
    for u in G:
        if (G.degree[u] > 1): #assumption: graph is connected. If degree = 1, C=0 (node cant be in a triangle)
            val = (triangles.get(u, 0)/2) * 2 / (G.degree[u] * (G.degree[u]-1)) #CC of node u
            #Note: divided by 2 because each triangle is counted twice in the dictionary. Thus dividing by 2 (and then multiplying by 2, due to CC formula)
            C += val
    C = C / len(G) #CC of graph: Average of CCs of nodes
    return C





