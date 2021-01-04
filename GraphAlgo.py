from heapq import *
from typing import List
from node_data import node_data
from GraphInterface import GraphInterface
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from typing import Deque
import queue


class GraphAlgo(GraphAlgoInterface):

    def __init__(self) -> None:
        self.g = DiGraph()

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
        heapify()
        heappush(src)
        while(he)


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass
