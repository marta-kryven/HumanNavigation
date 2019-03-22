import pdb, sys, numpy as np, pickle, os, cairo
import networkx as nx
from igraph import *
from matplotlib import pyplot as plt
from scipy.spatial import distance
import itertools
from itertools import count
#import custom functions
from custom_astar import astar_path, astar_path_length
from heuristics import *
from parse_graph import * #import test_graph_nx, data_graph_nx, test_graph, test_graph_bidirectional, and test_graph_node_positions

alpha = 0.5
beta = 1.0
source = 0
target = 100

#test algorith on a simple graph
path, path_length = astar_path_length(test_graph_nx, 0, 3, alpha, weighed_euclidean_distance(test_graph,beta))
x=plot_path(test_graph,test_graph_bidirectional, path, path_length, test_graph_node_positions)
x.show()

#test algorithm on the data
h = weighted_euclidean_distance(data_graph_nx, beta)
path, path_length = astar_path_length(data_graph_nx, source, target, alpha = alpha, h)

print 'path links: ', len(path)-1
print 'path length: ' , path_length

#test algorithm on a range of values
test_vals    = np.linspace(0,1,10)
N            = len(test_vals)
paths        = []
path_edges   = np.zeros([N,N])
path_lengths = np.zeros([N,N])
start_node   = 0
target_node  = 100

for i in range(N):
    alpha = test_vals[i]
    for j in range(N):
        beta = test_vals[j]
        h = weighted_euclidean_distance(data_graph_nx, beta)
        path, path_length = astar_path_length(data_graph_nx, 0, 100, alpha, heuristic = h)
        path_lengths[i,j] = path_length
        path_edges[i,j]   = len(path)-1
        
plt.imshow(path_lengths, interpolation='bilinear', origin='lower', extent=[0, 3, 0, 3])
plt.title('Path lengths for different alpha and betas\n Heuristic: Weighted Euclidean Distance');
plt.ylabel(r'$\alpha$')
plt.xlabel(r'$\beta$')
plt.colorbar()
plt.show()

plt.imshow(path_edges, interpolation='bilinear', origin='lower', extent=[0, 3, 0, 3])
plt.title('Path links for different parameters \n Heuristic: Weighted Euclidean Distance');
plt.ylabel(r'$\alpha$')
plt.xlabel(r'$\beta$')
plt.colorbar()
plt.show()
