import pdb, sys, numpy as np, pickle, os, cairo
import networkx as nx
from igraph import *
from matplotlib import pyplot as plt
from scipy.spatial import distance
import itertools
from itertools import count
#import custom functions
from custom_astar import astar_path, astar_path_length
from heuristics import weighed_euclidean_distance
from parse_graph import * #import test_graph_nx and data_graph_nx

alpha = 0.5
beta = 1.0
source = 0
target = 100

#test algorith on a simple graph
path, path_length = astar_path_length(test_graph_nx, 0, 3, alpha, weighed_euclidean_distance(test_graph,beta))
x=plot_path(test_graph,test_graph_bidirectional, path, path_length, test_graph_node_positions)
x.show()

#test algorithm on the data
path, path_length = astar_path_length(data_graph_nx, source, target, alpha = alpha, heuristic = weighed_euclidean_distance(data_graph_nx, beta))

print 'path links: ', len(path)-1
print 'path length: ' , path_length
