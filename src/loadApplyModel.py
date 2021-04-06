'''
Analysis to load road segments. 
The module also does some analysis (a form of betweenness centrality) 
but is not needed if networkOuput is used to launch the module.
 
Created on Nov 7, 2018

__author__: 
__version__: 1.0

'''


'''
Imports needed for this module
'''
import sys
import os
import math
#import matplotlib.pyplot as plt
import networkx as nx
import graph
import csv
import pysal as ps

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QApplication
'''
container used for nodes analysed and not to duplicate
'''
oldNodes={}

'''
Nodes analysed in the graph and to check they are present
'''
nodes={}

'''
Links analyzed and check they are present
'''
links=[]

'''
Total nodes iterated
'''
nodesS=[]

'''
Container for links with their link weights
'''
linkz={}

'''
Container to reference link ids
'''
ids={}

'''
Load the data and creating the links for the network from street segment file. The method returns a graph with all edges in the street network.
@param fileName -- the shapefile name to assess.
@return G- the network
'''
def load(fileName):
    
   
    
    shp = ps.lib.io.open(fileName[0])

    node1=0
    node2=0
    i = 1
    
    for s in shp:

        
        for p in s._vertices:
           
            node1=p[0]
            nodesS.append(node1)
            
            s1=str(str(node1[0])+":"+str(node1[1]))
            
            node2=p[1]
            s2=str(str(node2[0])+":"+str(node2[1]))
            
            bol=inNodes(node1,nodes)
            if bol is False:
                nodes[node1[0]]=node1[1]
                oldNodes[s1]=node1
            
            else:
                node1=oldNodes[s1]
            
            bol2=inNodes(node2,nodes)
            if bol2 is False:
                nodes[node2[0]]=node2[1]
                oldNodes[s2]=node2
            
            else:
                node2=oldNodes[s2]
                  
            weight=math.sqrt(math.pow(node1[0]-node2[0],2)+math.pow(node1[1]-node2[1],2))
            link=(node1,node2,weight)
            link2=(node1,node2)
            links.append(link)
            linkz[link2]=link
            ids[link2]=s.id
           
                
                
        
        i+=1
    
     
    G=graph.addWeightedEdges(links)
    
    return G
    
'''
Applying the shortest path algorithm from each point of the road segments
@param G-- the road network/graph representation.
@return edgesS- The edges from the network
'''
def runLinks(G):

    nodes=G.nodes
    nodes2=G.nodes
#    pos = nx.spring_layout(G)
#   nx.draw(G,pos,node_color='k')
    edgesS={}
    for n in nodes:
        for n2 in nodes2:
            if n2==n:
                continue
            else:
                path=nx.astar_path(G, n, n2, heuristic=None, weight='weight')
                path_edges = zip(path,path[1:])
                
                for e in path_edges:
                    if str(e) in edgesS:
                        nn=edgesS[str(e)]
                        edgesS[str(e)]=nn+1
                    else:
                        edgesS[str(e)]=1
                    
                    
    return edgesS
        
    
'''
Method to do the output of the links travelled, providing the network as output.
@param outputFolder- the output folder to put the results.csv file in
@param edgesS- the edges to produce the traveresed outputs from the overall street graph.
@param G- the network that is assessed
@return G- the network
'''
def output(outputFolder,edgesS,G):

    #pn='/home/mark/Papers/New_Book/Documents/Chapter2/dura_europas/'
   
    filename=os.path.join(outputFolder[0],'results.csv')
        
    fieldnames = ['id','x','y','count']
        
    with open(filename, 'w') as csvf:
        writer = csv.DictWriter(csvf, fieldnames=fieldnames)

        writer.writeheader()
            
        
        for ie in linkz:
            count=edgesS[str(ie)]
            link=linkz[ie]
            node1=link[0]
            node2=link[1]
            i=ids[(node1,node2)]
            writer.writerow({'id':i,'x':str(node1[0]),'y':str(node1[1]), 'count' :str(count)})
            writer.writerow({'id':i,'x':str(node2[0]),'y':str(node2[1]), 'count' :str(count)})
           
            print("Edges:"+ str(ie))
        
#    nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='r')
#    nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=10)
#    plt.axis('equal')
#    plt.show()
        
    return G
        
'''
Method for checking to see if the nodes already part of the road network
@param node-- the node to check
@param nodes-- the container for the nodes to check from.
@return iNodes= boolean if node a=node b
'''
def inNodes(node, nodes):

    iNodes=False
    if node[0] in nodes:
            y=node[1]
            if nodes[node[0]]==y:
                iNodes=True
                
    return iNodes

'''
Method to call and run the analysis.
'''
def run():
    
    app = QApplication(sys.argv)
    
    qid = QFileDialog()
#    fileName = "Enter the file to analyise here."
    filename=QFileDialog.getOpenFileName()

#    outputFolder = "Enter the output folder location here."
 #   mode = QLineEdit.Normal
#    text, ok = QInputDialog.getText(qid,outputFolder,fileName, mode)
 #   text2 = QInputDialog.getText(qid,filename[0], outputFolder, mode)
    paths=[]
    pn=os.path.abspath(__file__)
    pn=pn.split("src")[0]
    path=os.path.join(pn,'output')
    paths.append(path)
    paths.append(pn)
    
    text2 = QInputDialog.getItem(qid,"Folder Dialog", "Select Folder", paths, 0, False)
  

    G=load(filename)
    edgesS=runLinks(G)
    output(text2,edgesS,G)

if __name__ == '__main__':
    run()