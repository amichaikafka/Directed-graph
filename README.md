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


## Classes
### node_data
This class  represents the set of operations applicable on a
node (vertex) in a (directional) weighted graph.

### DiGraph
This class implements GraphInterface interface represents a directional weighted graph.
can support a large number of nodes (over 100,000).
The implementation using a dict.

### GraphAlgo
This class implements the GraphAlgoInterface interface including:
1. init(graph);
2. connected_components(); - the connected_components of a graph
3. connected_component(id1) -the connected_component that id1 belong to in the graph
4. shortest_path( src,  dest);using Dijkstra algorithm;
5. save_to_json(file); - JSON file
6. load_from_json(file); - JSON file
7. plot_graph()- display of the graph

## Interfaces
* GraphInterface
* GraphAlgoInterface

## Description of the main classes 
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

### connected_component 
 finds the Strongly Connected Component(SCC) that node id1 is a part of. (If the graph is None or id1 is not in the graph, the function should return an empty list []).

### connected_components
finds all the Strongly Connected Component(SCC) in the graph. (If the graph is None the function should return an empty list []).

### shortest_path
returns the the shortest path between src to dest using Dijkstra algorithm- as an ordered List of nodes:
src-- n1--n2--...dest
if no such path -- returns null;

## Correctness
Importent thing is to make sure that our implementions of the main algorithms is correct, 
therfore we compard our result of the implementions whith the result from networkx libary on large variety of graphs
from 10 vertex and 80 edges up to 30000 vertex and 240000 edges.
* The test:
```
   def test_correctness(self):
        """
        This test check the correctness of shortest path and connected_component
        by compare it to the results from networkx on the same graph.
        :return:None
        """
        ga = GraphAlgo.GraphAlgo()
        filename = '../data/G_30000_240000_1.json'
        ga.load_from_json(filename)
        ganx = self.graph_nx(ga.get_graph())

        l = ga.shortest_path(0, 2)

        l2 = nx.single_source_dijkstra(ganx, 0, 2)
        self.assertEqual(l,l2)
        l=ga.connected_components()

        l2=list(nx.strongly_connected_components(ganx))

        for i in range(len(l)):
            l[i].sort()
            self.assertTrue(set(l[i]) in l2)
```



