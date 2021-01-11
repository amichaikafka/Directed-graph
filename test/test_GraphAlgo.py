import unittest
from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.GraphInterface import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface

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
        l = [0, 1, 2, 3]
        lst = ga.connected_component(0)
        self.assertEqual(lst, l)

    def test_connected_components(self):
        g = self.create_graph()
        ga = GraphAlgo.GraphAlgo(g)
        l = [[0, 1, 2, 3], [4], [5], [6], [7, 8, 9], [10]]
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

    def test_plot_graph(self):
        g = self.create_graph()
        ga = GraphAlgo.GraphAlgo(g)
        ga.plot_graph()
