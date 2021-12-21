import networkx as nx
import numpy as np

def kclique_communities_detection(G,k):
    #Will implement the percolation method
    # maximal_cliques_edges = list(nx.find_cliques(G)) #get all maximal cliques (edges)
    maximal_cliques_nodes = list(nx.find_cliques(G))
    maximal_cliques_nodes = np.array(maximal_cliques_nodes, dtype=list)

    if (len(maximal_cliques_nodes) == 0) or (len(max(maximal_cliques_nodes,key=len)) < k): #edge case
        return []

    n = len(maximal_cliques_nodes)
    mat = np.zeros((n,n))
    for i in range(0,n): #foreach two cliques i,j
        for j in range(i,n):
            if (i != j):
                val = len(np.intersect1d(maximal_cliques_nodes[i],maximal_cliques_nodes[j])) # get intersection size
                if (val < k-1): #Thresholding for non-diagonal
                    val = 0
                else:
                    val = 1

                mat[i][j] = val
                mat[j][i] = val
            else:
                if (len(maximal_cliques_nodes[i]) < k): #Thresholding for diagonal
                    mat[i][i] = 0
                else:
                    mat[i][i] = 1

    G2 = nx.Graph()
    for i in range(0,n): #Create adjacency matrix representing
        for j in range(i,n):
            if (mat[i][j] == 1):
                G2.add_edge(i,j)

    communities = []
    comps = nx.connected_components(G2)
    for comp in comps: #each connected component's cliques are a community
        comp_community = set()
        for clique_node in comp:
            for v in maximal_cliques_nodes[clique_node]:
                comp_community.add(v)
        communities.append(comp_community)

    return communities







