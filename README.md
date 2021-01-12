# ex3

Object Oriented Programming - assignment 4 (ex3) Python
This is the fourth and final project for the course
Object-oriented programming at Ariel University.

In this assignment we will thoroughly learn the basics of object-oriented programming in the Python language,
we will deal with weighted and directed graphs, but this time in Python (compared to previous assignments we wrote in JAVA).

We will first describe the structure of our project:
first part - the DiGraph class is implemented using GraphInterface
Second part - GraphAlgo inheritance from the abstract class GraphInterface
third part - Checking and comparing running times.

We will now detail some of the main functions
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
* scc - second dfs scan only here we start from the node that has the latest finishing time
        according to the stack we used in the dfs algorithm and for each node that all of his neighbors
        were discovered enter him to a list (cc) as connected_component


## Main Algorithms
### Dijkstra
this function implements the Dijkstra algorithm on the graph,
marking any node that has been visited and setting the weight to the distance from the src node (source node)
for each node, in this search, until destination node.

### DFS (Depth first search)
Implementaion of non recursive dfs algorithm scan the graph for each node
enter to a list to mark the discover time, when a node that all of his neighbors
were discoverd enter him to a stack.



