from scipy.spatial import distance

def weighed_euclidean_distance(G, beta):
    def h(neighbor, target):
        score = beta * distance.euclidean(neighbor,target)
        return score
    return h
