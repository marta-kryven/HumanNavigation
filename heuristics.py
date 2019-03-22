from scipy.spatial import distance

def weighed_euclidean_distance(G, beta):
    def h(neighbor, target):
        score = beta * distance.euclidean(neighbor,target)
        return score
    return h

def weighted_degree_centrality(G, alpha, r):
    def h(neighbor, target):
        neighbor_graph = nx.ego_graph(G, neighbor, r)
        degree_centrality = sum(nx.closeness_centrality(neighbor_graph).values())
        score = alpha * degree_centrality 
        return score
    return h
