'''
Module to hold the graph data used in networkx.
Created on Nov 8, 2018

@author: 
'''
import networkx as nx

'''
Method to create a network.
@return G- the network graph
'''
def createNetwork():
    G=nx.Graph()
    
    
    return G

'''
Method to add a weight to the graph
@param x- the weight to add
@return G- the network graph
'''
def addWeightedEdges(x):
    G=nx.Graph()
    G.add_weighted_edges_from(x)
    
    return G



