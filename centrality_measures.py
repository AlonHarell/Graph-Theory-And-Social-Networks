import networkx as nx


#Degree centraility measure, for node i in graph G. Unnormalized.
def degree_centrality(G,i):
    return G.degree[i]


#Closeness centraility measure, for node i in graph G. Unnormalized.
def closeness_centrality(G,i):
    distances = dict()
    distances[i] = 0
    distances_sum = 0
    for e in nx.bfs_edges(G,i): #bfs_edges(G,i) is an iterator over edges in G, in the order of BFS
        val = distances[e[0]]+1
        distances[e[1]] = val #for edge (u,v):  distance from i to v = distance from i to u + 1
        distances_sum += val
    return 1/distances_sum


#Betweeness centraility measure, for node i in graph G. Unnormalized.
def betweeness_centrality(G,i):
    toReturnSum = 0
    nodes_list = list(G)
    for j in range(0,len(nodes_list)):
        s = nodes_list[j] #for node s, so that s != i
        if (s != i):
            for k in range(j+1, len(nodes_list)): #Scanning for index j+1, so nodes_list[k] != nodes_list[j].
                # Note: Graph is undirected so all unique pairs s,t will be scanned eventually.
                t = nodes_list[k] # for node t, so that t != i and t != s
                if (t != i):
                    countpaths_i = 0 # shortest paths through i
                    countpaths = 0 # total shortest paths
                    sp_s_t = nx.all_shortest_paths(G,s,t)
                    try:
                        for path in sp_s_t: # Iterators sp_s_t returns all shortest paths. throws NetworkXNoPath if there arent any.
                            countpaths +=1
                            if (i in path):
                                countpaths_i+=1
                    except nx.NetworkXNoPath:
                        countpaths_i = 0
                    toReturnSum += countpaths_i / countpaths #adding to sum: sigma_s,t (i) / sigma_s,t
    return toReturnSum





