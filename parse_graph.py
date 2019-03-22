import pdb, sys, numpy as np, pickle, os, cairo
import networkx as nx
from igraph import *

'''
This script contains functions to load a data graph and to create a test graph.
Author: Josefina Correa <jcorream@mit.edu>
'''
def load_data():
    fn = 'graph_clusters_30m_bos.pk'
    with open(fn,'rb') as f:
        G_data = pickle.load(f)
    return G_data
def make_test_graph(edges, positions):
    G = Graph(edges)
    G.vs['pos']=positions
    G.es['weight']=[distance.euclidean(G.vs['pos'][i[0]], G.vs['pos'][i[1]]) for i in edges]
    G.vs['names']=[str(i) for i in G.vs.indices] #for plotting vertex index
    G.es['names']=[str(np.round(i,2)) for i in G.es['weight']] #for plotting edge value
    return G
def convert_to_nx(G):
    nx_G = nx.Graph(G.get_edgelist())
    for n in nx_G.nodes:
        nx_G.nodes[n]['pos'] = G.vs['pos'][n]
    for e in nx_G.edges:
        nx_G[e[0]][e[1]]['weight'] = G.es.find(_between = ((e[0],),(e[1],)))['weight']
    return nx_G
def plot_path(G,G_bi,path,path_length,pos):
    print 'path:' , path, 'path length: ', path_length
    G_bi.es['color']='black'
    for i in range(len(path)-1):
        G_bi.es.find(_between = ((path[i],),(path[i+1],)) )['color'] = 'blue'
    return plot(G_bi, layout = pos, vertex_label = G.vs['names'],margin=150, bbox=(750,750))


test_graph_edges_bidirectional =[(0,1),(6,11),(11,6),
          (2,11),(1,5),(1,2),(2,1),(3,2),(2,3),(0,4),(4,5),(5,2),(4,6),(6,7),(7,8),(8,9),(9,10),(10,3),(7,11),(11,3)] #for visualization purposes
test_graph_edges_undirected  = [(0,1),(1,2),(1,5),(2,3),(0,4),(4,5),(5,2),(4,6),(6,7),(6,11),(7,8),(8,9),(9,10),(10,3),(7,11),(11,3)]
test_graph_node_positions = [(10,10),(0,10),(0,0),(10,0),(10,6),(0,6),(6,6),(6,4),(8.5,3),(9,2),(10,2),(6,0)]
test_graph_bidirectional =make_test_graph(test_graph_edges_bidirectional,test_graph_node_positions) #for visualization purposes

test_graph = make_test_graph(test_graph_edges_undirected,test_graph_node_positions)

test_graph_nx = convert_to_nx(test_graph)
data_graph_nx = convert_to_nx(load_data())

x=plot_path(G_h2,G_h2_bi, path, path_length, h2_ps)
