from scipy.spatial import distance
import networkx as nx

def weighted_centrality(G, beta):
    def h(neighbor, target):
        centrality     = sum(list(G.neighbors(neighbor)))
        score          = (alpha * centrality) 
        return score
    return h

def weighted_clustering_coefficient(G, alpha, r):
    def h(neighbor, target):
        neighbor_graph = nx.ego_graph(G, neighbor, r)
        clustering_coefficient = sum(nx.clustering(neighbor_graph).values())
        score = alpha * clustering_coefficient 
        return score
    return h

def weighted_euclidean_distance(G, beta):
    def h(neighbor, target):
        score = beta * distance.euclidean(neighbor,target)
        return score
    return h
