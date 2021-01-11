from unittest import TestCase
import unittest
from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.GraphInterface import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from src.node_data import node_data


class TestDiGraph(TestCase):
    def create_graph(self) -> DiGraph:
        g = DiGraph()
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

    def test_v_size(self):
        g = self.create_graph()
        self.assertEqual(11,g.v_size())
        g.remove_node(0)
        self.assertEqual(10, g.v_size())

    def test_e_size(self):
        g = self.create_graph()
        self.assertEqual(18, g.e_size())
        g.remove_node(0)
        self.assertEqual(16, g.e_size())

    def test_get_all_v(self):
        g = self.create_graph()
        for k,v in g.get_all_v().items():
            self.assertEqual(k,v.getkey())

    def test_all_in_edges_of_node(self):
        g = self.create_graph()
        l=[6,9]
        lst=[]
        for i in g.all_in_edges_of_node(7).keys():
            lst.append(i)
        self.assertEqual(l,lst)

    def test_all_out_edges_of_node(self):
        g = self.create_graph()
        l = []
        lst=[]
        for i in g.all_out_edges_of_node(5).keys():
            lst.append(i)
        self.assertEqual(l, lst)
        g.add_edge(5,3,10)
        g.add_edge(5, 4, 10)
        l = [3,4]
        lst = []
        for i in g.all_out_edges_of_node(5).keys():
            lst.append(i)
        self.assertEqual(l, lst)
        g.remove_node(5)
        l = []
        lst = []
        for i in g.all_out_edges_of_node(5).keys():
            lst.append(i)
        self.assertEqual(l, lst)

    def test_add_edge(self):
        g = self.create_graph()
        self.assertEqual(18, g.e_size())
        g.add_edge(0,8,2)
        self.assertEqual(19, g.e_size())
        g.add_edge(0, 8, 2)
        self.assertEqual(19, g.e_size())


    def test_add_node(self):
        g = self.create_graph()
        self.assertEqual(11, g.v_size())
        g.add_node(100)
        self.assertEqual(12, g.v_size())
        g.add_node(0)
        self.assertEqual(12, g.v_size())

    def test_remove_node(self):
        g = self.create_graph()
        self.assertEqual(11, g.v_size())
        self.assertEqual(18, g.e_size())
        g.remove_node(0)
        self.assertEqual(10, g.v_size())
        self.assertEqual(16, g.e_size())
        g.remove_node(0)
        self.assertEqual(10, g.v_size())
        self.assertEqual(16, g.e_size())
        g.add_node(0)
        self.assertEqual(11, g.v_size())
        self.assertEqual(16, g.e_size())

    def test_remove_edge(self):
        g = self.create_graph()
        self.assertEqual(18, g.e_size())
        g.remove_edge(7,8)
        self.assertEqual(17, g.e_size())
        g.remove_edge(0,3)
        self.assertEqual(17, g.e_size())
        g.remove_edge(0,2)
        self.assertEqual(16, g.e_size())
        g.remove_edge(7, 8)
        self.assertEqual(16, g.e_size())
