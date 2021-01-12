# ex3

Object Oriented Programming - assignment 4 (ex3) Python
This is the fourth and final project for the course
Object-oriented programming at Ariel University.

In this assignment we will thoroughly learn the basics of object-oriented programming in the Python language,
we will deal with weighted and directed graphs, but this time in Python (compared to previous assignments we wrote in JAVA).

### We will first describe the structure of our project:
* first part - the DiGraph class is implemented using GraphInterface
* Second part - GraphAlgo inheritance from the abstract class GraphInterface
* third part - Checking and comparing running times.

We will now detail some of the main functions:
### DiGraph
* add_node - Adds a node to the graph by the node ID.
* remove_node - removes a node from the graph.
* remove_edge - removes an edge from the graph.
* get_all_v - return a dictionary of all the nodes in the Graph, each node is represented using a pair(node_id, node_data).
* e_size - returns the number of edges in this graph.
* v_size - returns the number of vertices in this graph.

### GraphAlgo
* shortest_path - returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm.
* load_from_json - loads a graph from a json file.
* save_to_json - saves the graph in JSON format to a file.
* transpose - Transpose this graph: for every edge (u,v) make it (v,u) this is part of the algorithm of finding connected component.
* connected_component - finds the Strongly Connected Component(SCC) that node id1 is a part of. (If the graph is None or id1 is not in the graph, the function should return an empty list []).
* connected_components - finds all the Strongly Connected Component(SCC) in the graph. (If the graph is None the function should return an empty list []).
* plot_graph - Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.




## Main Algorithms
### Dijkstra
this function implements the Dijkstra algorithm on the graph,
marking any node that has been visited and setting the weight to the distance from the src node (source node)
for each node, in this search, until destination node.

### DFS (Depth first search)
Implementaion of non recursive dfs algorithm scan the graph for each node
enter to a list to mark the discover time, when a node that all of his neighbors
were discoverd enter him to a stack.

### scc 
second dfs scan only here we start from the node that has the latest finishing time
according to the stack we used in the dfs algorithm and for each node that all of his neighbors
were discovered enter him to a list (cc) as connected_component.

### scc2
this function uesd only for connected_component for particular node
second dfs scan only here we start from the node that has the latest finishing time
according to the stack we used in the dfs algorithm and for each node that all of his neighbors
were discovered enter him to a list (cc) as connected_component.



