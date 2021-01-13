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
import matplotlib.pyplot as plt
import numpy as np

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
        """
        this test check the correctness of get_graph function
        :return:None
        """
        g = self.create_graph()

        print(g)
        # print("dfgsfbfgbgfd")
        ga = GraphAlgo.GraphAlgo(g)
        print(ga.get_graph())
        self.assertEqual(ga.get_graph(), g)

    def test_save_load_to_json(self):
        """
        this test check the correctness of save and load functions
        :return:None
        """
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
        """
        this test check the correctness of transpose function
        :return:None
        """
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
        """
        this test check the correctness of connected_component function
        :return:None
        """
        g = self.create_graph()
        ga = GraphAlgo.GraphAlgo(g)
        l = [0,1,2,3]
        lst = ga.connected_component(0)
        lst.sort()
        self.assertEqual(lst, l)
        l = []
        lst = ga.connected_component(99)
        self.assertEqual(lst, l)

    def test_connected_components(self):
        """
        this test check the correctness of connected_components function
        :return:None
        """
        g = self.create_graph()
        ga = GraphAlgo.GraphAlgo(g)
        l = [[0,1,2,3], [6], [4], [7,8,9], [10], [5]]
        lst = ga.connected_components()
        for i in lst:
            i.sort()
            self.assertTrue(i in l)



    def test_shortest_path(self):
        """
        this test check the correctness of shortest path function
        :return:None
        """
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
        """
        this test check the run time of connected_components and shortest path
        :return:None
        """
        ga = GraphAlgo.GraphAlgo()
        filename='../data/G_30000_240000_1.json'
        ga.load_from_json(filename)


        with self.elapsed_timer() as elapsed:
            star = elapsed()
            l=ga.shortest_path(0,2)
            print(l[1])
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
        """
        this test check the run time of connected_components and shortest path
        in networkx
        :return:None
        """
        ga1 = GraphAlgo.GraphAlgo()
        filename = '../data/G_100_800_1.json'
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
                    print(list(nx.kosaraju_strongly_connected_components(ga)))

                    end = elapsed()
                    res = end - star

                    f.write(f"\ngraph:{filename},connected_component:{res}\n")

            except IOError as e:
                print(e)

    def test_correctness(self):
        """
        This test check the correctness of shortest path and connected_component
        by compar it to the results from networkx on the same graph.
        :return:None
        """
        ga = GraphAlgo.GraphAlgo()
        filename = '../data/G_20000_160000_1.json'
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
    def test_myplot(self):
        labels = ['|V|=10 |E|=80', '|V|=100 |E|=800', '|V|=1000 |E|=8000', '|V|=10000 |E|=80000', '|V|=20000 |E|=160000','|V|=30000 |E|=24000']
        networkx = [0.00018209999999996285, 0.0007703000000000015, 0.02424729999999986, 0.4630350999999999,1.8605402,4.058448499999999]
        # python = [0.00013769999999990734, 0.0013769000000000142,0.026254600000000017, 0.3735894000000002, 0.8037356,1.5485729]
        python = [0.0002621999999999902, 0.0015903999999999918, 0.04709249999999998, 1.0833412999999998, 5.090948099999999,
                  13.6692781]
        # java = [0.001, 0.003,0.019, 0.237, 0.52,0.98]
        java = [0.001, 0.004, 0.039, 0.657, 2.958, 8.057]

        x = np.arange(len(labels))  # the label locations
        width = 0.25  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width, networkx, width, label='networkx')
        rects2 = ax.bar(x, python, width, label='python')
        rects3 = ax.bar(x + width, java, width, label='java')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('seconds')
        ax.set_title('connected_components')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()



        fig.tight_layout()

        plt.show()