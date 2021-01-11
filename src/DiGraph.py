from src.GraphInterface import GraphInterface

from src.node_data import node_data


class DiGraph(GraphInterface):

    def __init__(self) -> None:
        """

        :rtype: object
        """
        self.edgesize = 0
        self.MC = 0
        self.Nodes = {}
        self.Edges = {}

    def v_size(self) -> int:
        """
               Returns the number of vertices in this graph
               @return: The number of vertices in this graph
               """
        return len(self.Nodes)

    def __eq__(self, o: object) -> bool:
        """
                   Comparison function.
                   """
        if not (isinstance(o, DiGraph)):
            return False
        if not (o.Edges.__eq__(self.Edges)):
            return False
        if not (o.Nodes.__eq__(self.Nodes)):
            return False
        return True

    def __str__(self) -> str:
        """
                       This method returns the string representation of the object.
                       """
        s = "Edeges{"
        for k, v in self.Edges.items():
            for i, j in v.items():
                s += f"[src:{k},w:{j},dest:{i}]"
        s += "} Nodes{"
        for i in self.Nodes.values():
            s += f"[{i}]"
        s += "}"
        return s

    def __repr__(self) -> str:
        """
         returns the object representation in string format.
        """
        s = "Edeges{"
        for k, v in self.Edges.items():
            for i, j in v:
                s += f"[src:{k},w:{j},dest:{i}]"
        s += "} Nodes{"
        for i in self.Nodes.values():
            s += f"[{i}]"
        s += "}"
        return s

    def getnode(self, id: int) -> node_data:
        """
                returns the node by the node ID.
               """
        return self.Nodes[id]

    def e_size(self) -> int:
        """
               Returns the number of edges in this graph
               @return: The number of edges in this graph
               """
        return self.edgesize

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
                (node_id, node_data)
               """
        return self.Nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
                each node is represented using a pair (other_node_id, weight)
                 """
        if id1 in self.Nodes:
            ans = {}
            for i, j in self.Edges.items():
                if id1 in j:
                    ans[i] = j[id1]
            return ans
        return {}

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
                (other_node_id, weight)
                """
        if id1 in self.Nodes:
            return self.Edges[id1]
        return {}

    def get_mc(self) -> int:
        """
               Returns the current version of this graph,
               on every change in the graph state - the MC should be increased
               @return: The current version of this graph.
               """
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        return: True if the edge was added successfully, False otherwise.
        :rtype: object
        """
        if id1 in self.Nodes and id2 in self.Nodes and id2 not in self.Edges[id1]:
            if self.Edges[id1] is None:
                self.Edges[id1] = {}
                self.Edges[id1][id2] = weight
            else:
                self.Edges[id1][id2] = weight
            self.edgesize += 1
            self.MC += 1
            return True
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """"
        Adds a node to the graph.
        """
        n = node_data(id=node_id, p=pos)
        self.Nodes[node_id] = n
        self.Edges[node_id] = {}

    def remove_node(self, node_id: int) -> bool:
        """
                Removes a node from the graph.
                Note: if the node id does not exists the function will do nothing
         """
        if node_id in self.Nodes:
            out = self.all_out_edges_of_node(node_id)
            to = self.all_in_edges_of_node(node_id)
            self.MC += len(self.Edges[node_id])
            self.edgesize -= len(self.Edges[node_id])
            del (self.Edges[node_id])
            # for k in out.keys():
            #     self.remove_edge(node_id, k)
            for k in to.keys():
                self.remove_edge(k, node_id)
            # self.Edges.pop(node_id)
            self.Nodes.pop(node_id)
            self.MC += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
                Removes an edge from the graph.
                Note: If such an edge does not exists the function will do nothing
                """
        if node_id1 in self.Nodes and node_id2 in self.Nodes and node_id2 in self.Edges[node_id1]:
            self.Edges[node_id1].pop(node_id2)
            self.edgesize -= 1
            self.MC += 1
            return True
        else:
            return False
