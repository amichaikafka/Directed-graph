import unittest
from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.GraphInterface import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
import time
from contextlib import contextmanager
from timeit import default_timer
import networkx as nx
import math

from src import *


class TestGraphAlgo(unittest.TestCase):

    def create_graph(self) -> DiGraph:
        g = DiGraph.DiGraph()
        for i in range(11):
            g.add_node(i)
        g.add_edge(0, 2, 1)
        g.add_edge(1, 2, 1)
        g.add_edge(1, 5, 1)
        g.add_edge(1, 6, 1)
        g.add_edge(2, 0, 1)
        g.add_edge(2, 3, 1)
        g.add_edge(3, 1, 1)
        g.add_edge(3, 4, 1)
        g.add_edge(3, 5, 1)
        g.add_edge(4, 8, 5)
        g.add_edge(6, 4, 0.5)
        g.add_edge(6, 7, 1)
        g.add_edge(7, 8, 1)
        g.add_edge(7, 9, 1)
        g.add_edge(8, 9, 1)
        g.add_edge(9, 8, 1)
        g.add_edge(9, 10, 1)
        g.add_edge(9, 7, 1)
        return g

    def test_get_graph(self):
        g = self.create_graph()

        print(g)
        # print("dfgsfbfgbgfd")
        ga = GraphAlgo.GraphAlgo(g)
        print(ga.get_graph())
        self.assertEqual(ga.get_graph(), g)

    def test_save_load_to_json(self):
        g = self.create_graph()
        ga = GraphAlgo.GraphAlgo(g)
        print(ga.get_graph())
        ga.save_to_json("gtest.json")
        ga.g = DiGraph.DiGraph()
        print(ga.get_graph())
        self.assertNotEqual(ga.get_graph(), g)
        ga.load_from_json("gtest.json")
        print(ga.get_graph())
        self.assertEqual(ga.get_graph(), g)

    def test_transpose(self):
        g = self.create_graph()
        print(g)
        ga = GraphAlgo.GraphAlgo(g)
        ga.transpose()
        print(ga.get_graph())
        self.assertNotEqual(ga.get_graph(), g)
        ga.transpose()
        print(ga.get_graph())
        self.assertEqual(ga.get_graph(), g)

    def test_connected_component(self):
        g = self.create_graph()
        ga = GraphAlgo.GraphAlgo(g)
        l = [3,1,2,0]
        lst = ga.connected_component(0)
        self.assertEqual(lst, l)
        l = []
        lst = ga.connected_component(99)
        self.assertEqual(lst, l)

    def test_connected_components(self):
        g = self.create_graph()
        ga = GraphAlgo.GraphAlgo(g)
        l = [[3, 1, 2, 0], [6], [4], [9, 7, 8], [10], [5]]
        lst = ga.connected_components()
        self.assertEqual(lst, l)

    def test_shortest_path(self):
        g = self.create_graph()
        ga = GraphAlgo.GraphAlgo(g)
        l = (6, [0, 2, 3, 1, 6, 7, 8])
        lst = ga.shortest_path(0, 8)
        self.assertEqual(l, lst)
        ga.get_graph().add_edge(6, 8, 1)
        l = (5, [0, 2, 3, 1, 6, 8])
        lst = ga.shortest_path(0, 8)
        self.assertEqual(l, lst)
        l=(math.inf,[])
        lst = ga.shortest_path(0, 99)

        self.assertEqual(l, lst)

    def test_plot_graph(self):
        g = self.create_graph()
        ga = GraphAlgo.GraphAlgo(g)
        ga.plot_graph()

    @contextmanager
    def elapsed_timer(self):
        start = default_timer()
        elapser = lambda: default_timer() - start
        yield lambda: elapser()
        end = default_timer()
        elapser = lambda: end - start
    def graph_nx(self,graph:DiGraph):
        g=nx.DiGraph()
        for i in graph.get_all_v().keys():
            g.add_node(i)
            for n,w in graph.all_out_edges_of_node(i).items():
                g.add_edge(i,n,weight=w)
        return g



    def test_algo_time(self):
        ga = GraphAlgo.GraphAlgo()
        filename='../data/G_30000_240000_1.json'
        ga.load_from_json(filename)


        with self.elapsed_timer() as elapsed:
            star = elapsed()
            l=ga.shortest_path(0,2)
            end = elapsed()
            res=end - star
            try:
                with open("res.txt", "a") as f:
                    f.write(f"\ngraph:{filename},shortest_path:{res}\n{l}")
                    star = elapsed()
                    l=ga.connected_component(0)
                    end = elapsed()
                    res = end - star

                    f.write(f"\ngraph:{filename},connected_component:{res}\n")
                    star = elapsed()
                    l=ga.connected_components()
                    end = elapsed()
                    res = end - star

                    f.write(f"\ngraph:{filename},connected_components:{res}\n")
            except IOError as e:
                print(e)

    def test_algo_time_nx(self):
        ga1 = GraphAlgo.GraphAlgo()
        filename = '../data/G_30000_240000_1.json'
        ga1.load_from_json(filename)
        ga=self.graph_nx(ga1.get_graph())

        with self.elapsed_timer() as elapsed:
            star = elapsed()

            l = nx.single_source_dijkstra(ga, 0, 2)
            end = elapsed()
            res = end - star
            try:
                with open("res2.txt", "a") as f:
                    f.write(f"\ngraph:{filename},shortest_path:{res}\n{l}")
                    star = elapsed()
                    # print(list(nx.strongly_connected_components(ga)))
                    print(nx.kosaraju_strongly_connected_components(ga))

                    end = elapsed()
                    res = end - star

                    f.write(f"\ngraph:{filename},connected_component:{res}\n")

            except IOError as e:
                print(e)

