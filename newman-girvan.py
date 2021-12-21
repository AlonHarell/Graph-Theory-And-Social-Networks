import networkx as nx

def graph_betweeness_list(G):
    betweeness_dict = nx.edge_betweenness_centrality(G)  # Creates dict of betweeness
    betweeness_lst = []
    for e in betweeness_dict:
        betweeness_lst.append((betweeness_dict[e], e))
    betweeness_lst.sort()  # Gets a sorted list of tuples (betweeness, edge) sorted by betweeness
    return betweeness_lst

def newman_girvan(G,k):
    copyG = G.copy()

    if (k == 1):
        return list({copyG.nodes()})

    betweeness_lst = graph_betweeness_list(copyG)  #getting a sorted list of betweeneses
    if (len(betweeness_lst) == 0): #edge case: no edges at all
        if (len(G) == k):
            return list({copyG.nodes()})

    while (len(betweeness_lst) != 0):
        e = betweeness_lst[len(betweeness_lst)-1][1] #Always sorted, so last item has max value
        copyG.remove_edge(e[0], e[1])
        num_connected = nx.number_connected_components(copyG)
        if (num_connected == k): #if k connected components, they are our communities
            return list(nx.connected_components(copyG))
        betweeness_lst = graph_betweeness_list(copyG)

    return []


