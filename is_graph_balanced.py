import networkx as nx


#Recieves a graph. Returns True iff G is balanced.
def check_balance(G):
    plusG = nx.Graph() # Creating new graph, with only '+' edges
    minusSet = set() # Saving '-' edges
    for e in G.edges(data=True):
        if (e[2]['label'] == "+"):
            plusG.add_edge(e[0],e[1])
        if (e[2]['label'] == "-"):
            minusSet.add((e[0],e[1]))
    components = list(nx.connected_components(plusG)) # Getting all connected components of '+' graph
    Gcon = nx.Graph() # Gcon is the "supergraph": each node represents a connected component in plusG
    for i in range(0,len(components)):
        Gcon.add_node(i)
    for e in minusSet: # for e=(u,v)
        comp_1 = -1 # sentinel, component of u
        comp_2 = -2 # sentinel, component of v
        for i in range(0,len(components)):
            if ((comp_1 == -1) and (e[0] in components[i])): # Found component of u
                comp_1 = i
            if ((comp_2 == -2) and (e[1] in components[i])): # Found component of v
                comp_2 = i
            if (comp_1 == comp_2): #If a minus edge in same comp, unbalanced.
                return False
            if ((comp_1 != -1) and (comp_2 != -2)): # Both components found, so should break
                break
        Gcon.add_edge(comp_1,comp_2) # adding minus edge between components

    return nx.is_bipartite(Gcon) # G is balanced iff Gcon is bipartite
