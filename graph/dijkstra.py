#https://atcoder.jp/contests/abc035/tasks/abc035_d

from collections import defaultdict
from heapq import heappop, heappush
 
class Graph():
 
    def __init__(self, directed=True):
        self.__graph = defaultdict(list)
        self.__vertices = set()
        self.__edges = []
        self.__directed = directed
 
    def add_edge(self, a, b, weight=1):
        self.__vertices |= {a, b}
        if self.__directed:
            self.__graph[a].append((b, weight))
            self.__edges.append((a, b, weight))
        else:
            self.__graph[a].append((b, weight))
            self.__graph[b].append((a, weight))
            self.__edges.append((a, b, weight))
            self.__edges.append((b, a, weight))

    @property
    def graph(self):
        return self.__graph
 
    @property
    def vertices(self):
        return sorted(list(self.__vertices))
    
    @property
    def edges(self):
        return self.__edges
 
    def num_of_vertices(self):
        return len(self.__vertices)
 
    def num_of_edges(self):
        if self.__directed:
            return len(self.__edges)
        else:
            return len(self.__edges)//2
 
class Dijkstra:
 
    def __init__(self, graph: Graph, start):
        self.__g = graph.graph
        self.__dist = defaultdict(lambda: float("inf"))
        self.__dist[start] = 0
        self.__prev = defaultdict(lambda: None)
        self.__Q = []
        heappush(self.__Q, (0, start))
 
        while self.__Q:
            dist_u, u = heappop(self.__Q)
 
            if self.__dist[u] < dist_u:
                continue
 
            for v, weight in self.__g[u]:
                alt = dist_u + weight
                if self.__dist[v] > alt:
                    self.__dist[v] = alt
                    self.__prev[v] = u
                    heappush(self.__Q, (alt, v))
 
 
    def shortest_distance(self, goal):

        return self.__dist[goal]
 
    def shortest_path(self, goal):

        path = []
        vertice = goal
        while vertice is not None:
            path.append(vertice)
            vertice = self.__prev[vertice]
 
        return path[::-1]