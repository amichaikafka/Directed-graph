from heapq import *
from typing import List
import random
import json
import networkx as nx
import pylab

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

    def __init__(self, g: GraphInterface = DiGraph()) -> None:
        self.g = g

    def init_graph(self, g: GraphInterface):
        self.g = g

    def get_graph(self) -> GraphInterface:
        return self.g

    def load_from_json(self, file_name: str) -> bool:
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
        try:
            with open(file_name, "w") as file:
                j = {}
                nodes = []
                edges = []
                for i in self.g.get_all_v().values():
                    if i.getlocation() is None:
                        nodes.append({"id": i.getkey()})
                    else:
                        nodes.append({"id": i.getkey(), "pos": str(i.getlocation())})
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
        p = {}
        unvisit = []
        for i in self.g.get_all_v().values():
            unvisit.append(i)
        src.setweight(0)
        heapify(unvisit)

        while len(unvisit) > 0:
            n = heappop(unvisit)
            n.settag(1)
            if n.__eq__(dest):
                return p
            for i, j in self.g.all_out_edges_of_node(n.getkey()).items():
                nei = self.g.getnode(i)

                if nei.gettag() == 0:
                    w = n.getweight() + j
                    if w < nei.getweight():
                        nei.setweight(w)
                        p[nei.getkey()] = n
                        heapify(unvisit)

        return p

    def initgraph(self) -> None:
        for i in self.g.Nodes.values():
            i.settag(0)
            i.setweight(math.inf)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
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

    def BFS(self, src: int, l: list, visited: dict) -> None:
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


    def dfs(self, n: node_data, stack: list, visited: dict) -> None:
        visited[n.getkey()] = True
        for i in self.g.all_out_edges_of_node(n.getkey()).keys():
            nei = self.g.getnode(i)
            if not visited[nei.getkey()]:
                self.dfs(n=nei, stack=stack, visited=visited)
        stack.append(n)

    def scc(self, n: node_data, cc: list, visited: dict) -> None:
        visited[n.getkey()] = True
        cc.append(n.getkey())
        for i in self.g.all_out_edges_of_node(n.getkey()).keys():
            nei = self.g.getnode(i)
            if not visited[nei.getkey()]:
                self.scc(n=nei, cc=cc, visited=visited)

    def transpose(self) -> None:
        graph = DiGraph()
        for i in self.g.get_all_v().keys():
            node = self.g.getnode(i)
            graph.add_node(i, node.getlocation())
            # print(node)
            graph.getnode(i).settag(node.gettag())
            # print(graph.getnode(i))
        for i in self.g.get_all_v().keys():
            for n, w in self.g.all_out_edges_of_node(i).items():
                graph.add_edge(n, i, w)
        self.g = graph

    def connected_component(self, id1: int) -> list:
        # visited = {}
        # for i in self.g.get_all_v().keys():
        #     visited[i] = False
        # stack = []
        # cc = []
        # idnode = self.g.getnode(id1)
        # for i in self.g.get_all_v().keys():
        #     i = self.g.getnode(i)
        #     if not visited[i.getkey()]:
        #         self.dfs(i, stack, visited)
        # # self.dfs(idnode, stack, visited)
        # for i in self.g.get_all_v().keys():
        #     visited[i] = False
        # self.transpose()
        # while stack:
        #     n = stack.pop()
        #     self.scc(n, cc, visited)
        #     if id1 in cc:
        #         self.transpose()
        #         return cc
        #     cc.clear()
        visited = {}

        for i in self.g.get_all_v().keys():
            visited[i] = False
        nei = []
        ccstart = []
        ccend = []
        ans = []
        self.BFS(src=id1, l=nei, visited=visited)
        ccstart = nei.copy()
        nei.clear()

        for i in self.g.get_all_v().keys():
            visited[i] = False
        self.transpose()
        self.BFS(src=id1, l=nei, visited=visited)
        ccend = nei.copy()
        nei.clear()
        ccstart.sort()

        for i in ccstart:
            if i in ccend:
                self.g.getnode(i).settag(1)
                ans.append(i)
        self.transpose()
        return ans

    def connected_components(self) -> List[list]:
        # stack = []
        # cc = []
        # ans = []
        # visited = {}
        # for i in self.g.get_all_v().keys():
        #     visited[i] = False
        # for i in self.g.get_all_v().keys():
        #     i = self.g.getnode(i)
        #     if not visited[i.getkey()]:
        #         self.dfs(i, stack, visited)
        # for i in self.g.get_all_v().keys():
        #     visited[i] = False
        # self.transpose()
        #
        # while stack:
        #     n = stack.pop()
        #     if not visited[n.getkey()]:
        #         self.scc(n, cc, visited)
        #         ans.append(cc.copy())
        #     # print(ans)
        #     cc.clear()
        # self.transpose()
        # return ans
        self.initgraph()
        stack = []
        ccstart = []
        cc = []
        ans = []
        visited = {}
        for i in self.g.get_all_v().keys():
            visited[i] = False
        for node in self.g.get_all_v().keys():
            # print(node)
            if not visited[node]:
                cc=self.connected_component(node)
                for v in cc:
                    visited[v]=True
                ans.append(cc)
                # print(node)
        return ans

    def plot_graph(self) -> None:
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
            for e,wi in self.g.all_out_edges_of_node(i.getkey()).items():
                n = self.g.getnode(e)
                if n.getlocation() is None:
                    v = random.uniform(0.0, 10000)
                    w = random.uniform(0.0, 10000)
                    pos = (v, w, 0)
                    n.setlocation(pos)

                v, w, z = n.getlocation()
                plt.annotate("", xy=(x, y), xytext=(v, w), arrowprops=dict(arrowstyle="<-"))
                plt.text((x+v)/2, (y+w)/2, str(wi), color="purple", fontsize=10)

        plt.show()
