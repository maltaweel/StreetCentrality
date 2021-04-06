Libraries Used

Python 3.6+ was used in development of this plugin. The following are the python libraries used:

pysal==2.0.0
pandas==1.0.5
networkx==2.4
numpy==1.19.5
Shapely==1.7.1
geopandas==0.9.0
PyQt4==4.11.4
PyQt5==5.15.4

Use pip install for the requirements.txt:  pip install -r requirements.txt

GitHub Repository for Street Centrality

Intent of Models

The Python project determines centrality (9 measures; betweeeness, closeness, degree, efficiency, eigenvector, harmonic, Katz, straightness, and current flow centrality). The key module, networkAnalysis.py, does most of the centrality measures. The analysis is, however, launched from networkOutput.py, which enables output data in .csv and .shp files. The shapefiles are for edges, while the .csv can be used for nodes. The shapefile edge centrality are mean values for two nodes in edges.

Users do not need to do anything except launch networkOutput.py and then select the file they want. The analysis is automated after this. Be sure to have Python 3.6+ installed. If using another version of Python, then edit the launch.sh file to fit the version of Python you have installed.

Data Requirements

To run the modules, you need to have a shapefile that has snapped street segments where each link is two nodes consisting of a start and end node. This will make the street segments a graph that is analysed in the modules. The outputs of the models are csv files that have the point data (the nodes) of the street segments that are then associated with a given analysis (e.g., number of times visited). Sample Data are provided within the project code (Sample_Data) but users can also use their own data.

Key Analysis Code:


Graph Analysis

In this analysis, a graph is created which is used to study the street network. This is applied in the networkAnalysis.py module. The different analyses applied are:  global network efficiency (, centrality measures, betweenness, closeness, degree, efficiency, straightness centrality. The results are provided as csv files (globalEfficiency, efficiencyCentrality, straightnessCentarlity, and nodeCentrality). The algorithm applies the methods as discussed in Port et al. (2006) for efficiency. Additionally, for centrality metrics calculated, Networkx is used. 

Other Folders

output: Data outputted from analysis conducted are placed here. Example output is given by default; however, if the user runs his/her analysis, the .csv and .shp outputs will automatically be placed in this folder.

Sample_Data: Sample street network data to test the analyses.
References:  This provides the references used to shape the algorithms applied and discussed above.

References

Altaweel, M; Wu, Y. (2010). Route selection and pedestrian traffic: applying an integrated modeling approach to understanding movement. Structure and Dynamics: eJournal of Anthropological and Related Sciences 4(2).Retrieved from https://escholarship.org/uc/item/6898p5vm.

Porta, S.; Pablo, C.;Vito, L. 2006. The Network Analysis of Urban Streets: A Primal Approach. Environment and Planning B: Planning and Design 33 (5): 705–25. https://doi.org/10.1068/b32045.






