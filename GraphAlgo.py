from heapq import *
from typing import List
import random

import networkx as nx
import pylab

from node_data import node_data
from GraphInterface import GraphInterface
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
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
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

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
        self.initgraph()
        src = self.g.getnode(id1)
        dest = self.g.getnode(id2)
        p = self.Dijkstra(src, dest)
        if id2 in p.keys():
            path = []
            path.append(id2)
            n = id2
            while n != id1:
                n = p[n].getkey()
                path.insert(0, n)
            return (dest.getweight(), path)
        return (float('inf'), [])

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        for i in self.g.get_all_v().values():
            x=y=0
            if i.getlocation() is None:
                x = random.uniform(0.0, 50)
                y = random.uniform(0.0, 50)
                pos=(x,y,0)
                i.setlocation(pos)

            x,y,z=i.getlocation()
            plt.plot(x, y, markersize=10, marker='.', color='blue')
            plt.text(x, y, str(i.getkey()), color="red", fontsize=12)
            for e in self.g.all_out_edges_of_node(i.getkey()).keys():
                n=self.g.getnode(e)
                if n.getlocation() is None:
                    v = random.uniform(0.0, 50)
                    w = random.uniform(0.0, 50)
                    pos = (v, w, 0)
                    n.setlocation(pos)

                v, w, z = n.getlocation()
                plt.annotate("", xy=(x, y), xytext=(v, w), arrowprops=dict(arrowstyle="<-"))

        plt.show()




