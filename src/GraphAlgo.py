from heapq import *
from typing import List
import random
import json
import networkx as nx
import pylab
import time
from contextlib import contextmanager
from timeit import default_timer
from src.node_data import node_data
from src.GraphInterface import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from typing import Deque
import queue
from queue import PriorityQueue
import math
import matplotlib.pyplot as plt
import numpy as np


class GraphAlgo(GraphAlgoInterface):
    """

    This class implements the GraphAlgoInterface interface including:
    1. init(graph);
    2. connected_components(); - the connected_components of a graph
    3. connected_component(id1) -the connected_component that id1 belong to in the graph
    4. shortest_path( src,  dest);using Dijkstra algorithm;
    5. save_to_json(file); - JSON file
    6. load_from_json(file); - JSON file
    7. plot_graph()- display of the graph

    """

    def __init__(self, g: GraphInterface = DiGraph()) -> None:
        self.g = g

    def init_graph(self, g: GraphInterface) -> None:
        """
        Init the graph on which this set of algorithms operates on.
        :param g:the graph
        :return:None
        """
        self.g = g

    def get_graph(self) -> GraphInterface:
        """
         :return: the directed graph on which the algorithm works on.
        """
        return self.g

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        graph = DiGraph()
        try:
            with open(file_name, "r") as file:
                my_d = json.load(file)
        except IOError as e:
            print(e)
            return False
        for i in my_d["Nodes"]:
            if "pos" not in i.keys():
                graph.add_node(node_id=i["id"])
            else:
                p = tuple(map(float, i["pos"].split(",")))
                graph.add_node(node_id=i["id"], pos=p)
        for edge in my_d["Edges"]:
            src = edge["src"]
            dest = edge["dest"]
            w = edge["w"]
            graph.add_edge(id1=src, id2=dest, weight=w)
        self.g = graph
        return True

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        try:
            with open(file_name, "w") as file:
                j = {}
                nodes = []
                edges = []
                for i in self.g.get_all_v().values():
                    if i.getlocation() is None:
                        nodes.append({"id": i.getkey()})
                    else:
                        nodes.append({"id": i.getkey(), "pos": str(str(i.getlocation()[0])+","+str(i.getlocation()[1])+","+str(i.getlocation()[2]))})
                    for v, k in self.g.all_out_edges_of_node(i.getkey()).items():
                        edges.append({"src": i.getkey(), "dest": v, "w": k})
                j["Nodes"] = nodes
                j["Edges"] = edges

                json.dump(j, indent=4, fp=file)
                return True
        except IOError as e:
            print(e)
            return False

    def Dijkstra(self, src: node_data, dest: node_data) -> dict:
        """
        this function implements the Dijkstra algorithm on the graph
        marking any node that has been visited and setting the weight to the distance from the src node (source node)
        for each node, in this search, until destination node .
        :param src:
        :param dest:
        :return:dict that contain every parent of each node (consider minimum distance )
        in this search starting at key (src) node.
        """
        p = {}
        unvisit = []

        unvisit.append(src)
        src.setweight(0)
        heapify(unvisit)

        while len(unvisit) > 0:
            n = heappop(unvisit)
            n.settag(1)
            if n == dest:
                return p
            for i, j in self.g.all_out_edges_of_node(n.getkey()).items():
                nei = self.g.getnode(i)

                if nei.gettag() == 0:
                    w = n.getweight() + j

                    if w < nei.getweight():
                        nei.setweight(w)
                        p[nei.getkey()] = n
                        heappush(unvisit, nei)

        return p

    def initgraph(self) -> None:
        """
        initialization of all the vertex, to avoid mistakes in the next operations.
        :return:None
        """
        for i in self.g.Nodes.values():
            i.settag(0)
            i.setweight(math.inf)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        Example:
       # >>> from GraphAlgo import GraphAlgo
       # >>> g_algo = GraphAlgo()
       # >>> g_algo.addNode(0)
       # >>> g_algo.addNode(1)
       # >>> g_algo.addNode(2)
       # >>> g_algo.addEdge(0,1,1)
       # >>> g_algo.addEdge(1,2,4)
       # >>> g_algo.shortestPath(0,1)
       # (1, [0, 1])
       # >>> g_algo.shortestPath(0,2)
       # (5, [0, 1, 2])
        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])

        """
        path = []
        if id1 in self.g.get_all_v() and id2 in self.g.get_all_v():
            self.initgraph()
            src = self.g.getnode(id1)
            dest = self.g.getnode(id2)

            p = self.Dijkstra(src, dest)

            if id2 in p.keys():

                path.append(id2)
                n = id2
                while n != id1:
                    n = p[n].getkey()
                    path.insert(0, n)
                return (dest.getweight(), path)
        return (float('inf'), path)

    def BFS(self, src: int, l: list, visited: dict, visited2: dict) -> None:
        q = []
        l.append(src)
        q.append(src)
        while q:
            n = q.pop(0)
            visited[n] = True
            for dest in self.g.all_out_edges_of_node(n).keys():
                if not visited[dest]:
                    visited[dest] = True
                    q.append(dest)
                    l.append(dest)

    def dfs(self, n: node_data, stack: list, visited: dict, visited2: dict) -> None:
        """
        Implementaion of non recursive dfs algorithm scan the graph for each node
        enter to a list to mark the discover time, when a node that all of his neighbors
        were discoverd enter him to a stack
        :param n: the node that start this scan
        :param stack: contain the node of this scan according to finishing time for each node
        :param visited: mark each node if visited to make sure we don't repeat on the same node
        :param visited2: mark each node that seen in the scan
        to avoid mistake in the scan after transpose the graph
        :return:None
        """
        visited[n.getkey()] = True
        discver = {}
        discver[n.getkey()] = 0
        t = 0
        lst = []
        lst.append(n.getkey())

        while lst:
            i = lst[-1]

            if i not in discver:
                t += 1
                discver[i] = t
            flag = True

            for neib in self.g.all_out_edges_of_node(i).keys():
                if neib not in discver:
                    lst.append(neib)
                    flag = False
                    break
            if flag:
                visited[i] = True
                visited2[i] = True
                stack.append(i)
                lst.pop()

    def scc(self, n: node_data, cc: list, visited: dict) -> None:
        """
        second dfs scan only here we start from the node that has the latest finishing time
        according to the stack we used in the dfs algorithm and for each node that all of his neighbors
        were discovered enter him to a list (cc) as connected_component
        :param n: the node that start this scan
        :param cc: list that save the connected_component
        :param visited:mark each node if visited to make sure we don't repeat on the same node
        :return:None
        """
        discver = {}
        discver[n.getkey()] = 0
        t = 0
        lst = []
        lst.append(n.getkey())
        while lst:
            i = lst[-1]

            if i not in discver:
                t += 1
                discver[i] = t
            flag = True
            for neib in self.g.all_out_edges_of_node(i).keys():
                if neib not in discver:
                    if visited[neib]:
                        continue
                    lst.append(neib)
                    flag = False
                    break
            if flag:
                visited[i] = True
                cc.append(i)
                lst.pop()

    def scc2(self, n: node_data, cc: list, visited: dict, visited2: dict = {}) -> None:
        """
        this function uesd only for connected_component for particular node
        second dfs scan only here we start from the node that has the latest finishing time
        according to the stack we used in the dfs algorithm and for each node that all of his neighbors
        were discovered enter him to a list (cc) as connected_component

        :param n:the node that start this scan
        :param cc:list that save the connected_component
        :param visited:mark each node if visited to make sure we don't repeat on the same node
        :param visited2:contain True only for node that were in the last dfs scan to avoid mistake
        :return:None
        """

        discver = {}
        discver[n.getkey()] = 0
        t = 0
        lst = []
        lst.append(n.getkey())
        while lst:
            i = lst[-1]

            if i not in discver:
                t += 1
                discver[i] = t
            flag = True
            for neib in self.g.all_out_edges_of_node(i).keys():
                if not visited2[neib]:
                    continue
                if neib not in discver:
                    if visited[neib]:
                        continue
                    lst.append(neib)
                    flag = False
                    break
            if flag:
                visited[i] = True
                cc.append(i)
                lst.pop()

    def transpose(self) -> None:
        """
        Transpose this graph: for every edge (u,v) make it (v,u)
        this is part of the algorithm of finding connected component
        :return:None
        """
        graph = DiGraph()
        for i in self.g.get_all_v().keys():
            node = self.g.getnode(i)
            graph.add_node(i, node.getlocation())

            graph.getnode(i).settag(node.gettag())

        for i in self.g.get_all_v().keys():
            for n, w in self.g.all_out_edges_of_node(i).items():
                graph.add_edge(n, i, w)
        self.g = graph

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        Notes:
        If the graph is None or id1 is not in the graph, the function should return an empty list []
        """
        if self.g is None or id1 not in self.g.get_all_v():
            return []
        visited = {}
        visited2 = {}
        for i in self.g.get_all_v().keys():
            visited[i] = False
            visited2[i] = False

        stack = []
        cc = []
        idnode = self.g.getnode(id1)

        self.dfs(idnode, stack, visited, visited2)

        for i in self.g.get_all_v().keys():
            visited[i] = False
        self.transpose()
        while stack:
            n = stack.pop()
            if not visited[n]:
                self.scc2(self.g.getnode(n), cc, visited, visited2)
                if id1 in cc:
                    self.transpose()
                    return cc
                cc.clear()

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        Notes:
        If the graph is None the function should return an empty list []
        """
        # if self.g is None:
        #     return []
        # visited = {}
        # visited2 = {}
        # for i in self.g.get_all_v().keys():
        #     visited[i] = False
        #     visited2[i] = False
        # stack = []
        # cc = []
        # ans = []
        #
        # for i in self.g.get_all_v().keys():
        #     i = self.g.getnode(i)
        #     if not visited[i.getkey()]:
        #         self.dfs(i, stack, visited, visited2)
        #
        # for i in self.g.get_all_v().keys():
        #     visited[i] = False
        # self.transpose()
        # while stack:
        #     n = stack.pop()
        #     if not visited[n]:
        #         self.scc2(self.g.getnode(n), cc, visited,visited2)
        #         print(cc)
        #         if cc not in ans:
        #             ans.insert(0,cc.copy())
        #         cc.clear()
        # self.transpose()
        # return ans
        if self.g is None:
             return []
        visited = {}

        cc = []
        ans = []

        for i in self.g.get_all_v().keys():
            visited[i] = False
        for i in self.g.get_all_v().keys():
            if not visited[i]:
                cc=self.connected_component(i)
                for n in cc:
                    visited[n]=True
                ans.append(cc.copy())
                cc.clear()
        return ans





    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        for i in self.g.get_all_v().values():
            x = y = 0
            if i.getlocation() is None:
                x = random.uniform(0.0, 10000)
                y = random.uniform(0.0, 10000)
                pos = (x, y, 0)
                i.setlocation(pos)

            x, y, z = i.getlocation()
            plt.plot(x, y, markersize=10, marker='.', color='blue')
            plt.text(x, y, str(i.getkey()), color="red", fontsize=12)
            for e, wi in self.g.all_out_edges_of_node(i.getkey()).items():
                n = self.g.getnode(e)
                if n.getlocation() is None:
                    v = random.uniform(0.0, 10000)
                    w = random.uniform(0.0, 10000)
                    pos = (v, w, 0)
                    n.setlocation(pos)

                v, w, z = n.getlocation()
                plt.annotate("", xy=(x, y), xytext=(v, w), arrowprops=dict(arrowstyle="<-"))
                # plt.text((x+v)/2, (y+w)/2, str(wi), color="purple", fontsize=10)

        plt.show()
