#ABC061D Score Attack

from collections import defaultdict
from heapq import heappop, heappush
 
class Graph:
 
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
        self.edges = []
 
    def add_edge(self, a, b, weight=1):
        self.graph[a].append((b, weight))
        self.vertices |= {a, b}
        self.edges.append((a, b, weight))
 
    def get_vertices(self):
        return sorted(list(self.vertices))
 
    def num_of_vertices(self):
        return len(self.vertices)
 
    def get_edges(self):
        return self.edges
 
    def num_of_edges(self):
        return len(self.edges)
 
class BellmanFord:
 
    def __init__(self, graph):
        self.num_of_vertices = graph.num_of_vertices()
        self.edges = graph.get_edges()
 
    def short_dist(self, start, goal):
        self.dist = defaultdict(lambda: float("inf"))
        self.dist[start] = 0
        for i in range(self.num_of_vertices):
            for edge in self.edges:
                if self.dist[edge[0]] != float("inf") and \
                self.dist[edge[1]] > self.dist[edge[0]] + edge[2]:
                    self.dist[edge[1]] = self.dist[edge[0]] + edge[2]
                    #負閉路検出
                    if i == self.num_of_vertices-1 and edge[1] == goal:
                        return float("inf")
        return self.dist[goal]