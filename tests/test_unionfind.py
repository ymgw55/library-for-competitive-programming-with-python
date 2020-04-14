import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from datastructure.unionfind import UnionFind
import unittest

class TestUnionFind(unittest.TestCase):
    """
    test class of UnionFind
    """

    def test_sample1(self):
        """
        test method for UnionFind

        at first, N is given and make a disjoint set whose elements are 0, 1,..., N-1, 
        and then Q and Query are given.
        Q is the size of Query and Query consits of (p1, x1, y1), (p2, x2, y2)...(pQ, xQ, yQ).
        p is the marker of the type of query and x, y are elements.


        the type of query:
        if p = 0, unite x and y.
        if p = 1, check whether x, y are united and return True or False.


        "expected" is the expected answer list, 
        and "output" is the output list which recodes boolean when p = 1.

        """

        N = 8
        U = UnionFind(N)

        Q = 9
        Query = [
            (0, 1, 2),
            (0, 3, 2),
            (1, 1, 3),
            (1, 1, 4),
            (0, 2, 4),
            (1, 4, 1),
            (0, 4, 2),
            (0, 0, 0),
            (1, 0, 0)
        ]
        expected = [True, False, True, True]
        output = []

        for i in range(Q):
            p, x, y = Query[i]
            if p:
                output.append((U.issame(x, y)))
            else:
                U.merge(x, y)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()