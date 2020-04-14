import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from graph.dijkstra import Graph, Dijkstra
import unittest

class TestDijkstra(unittest.TestCase):
    """
    test class of Dijkstra
    """
    def test_sample1(self):
        """

        test method for Dijkstra

        at first, V, E, and "start" are given.
        V is the number of vertices and E is the number of edges and "start" is the start vertice.
        then, edge infomation list "info" is given.
        the number of the elements of the list is E, and each elements consists of (s, t, d).
        this means the distance s to t is d.
        after reading the information, 
        check the distance from start vertice to each vertice (i.e. 0, 1,.., V-1).

        "expected" is the expected answer list, 
        and "output" is the output list for each vertice.

        """

        V, E, start = 4, 5, 0
        info = [
            (0, 1, 1),
            (0, 2, 4),
            (1, 2, 2),
            (2, 3, 1),
            (1, 3, 5)
        ]

        g = Graph()
        for s, t, d in info:
            g.add_edge(s, t, d)
        
        dijkstra = Dijkstra(g, start)

        expected = [0, 1, 3, 4]
        output = []
        for v in range(V):
            output.append(dijkstra.shortest_distance(v))
        
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()