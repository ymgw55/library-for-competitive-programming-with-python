#ABC035D トレジャーハント

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
 
class Dijkstra:
 
    def __init__(self, graph, start):
        self.g = graph.graph
 
        self.dist = defaultdict(lambda: float("inf"))
        self.dist[start] = 0
 
        self.prev = defaultdict(lambda: None)
 
        self.Q = []
        heappush(self.Q, (0, start))
 
        while self.Q:
            dist_u, u = heappop(self.Q)
 
            if self.dist[u] < dist_u:
                continue
 
            for v, weight in self.g[u]:
                alt = dist_u + weight
                if self.dist[v] > alt:
                    self.dist[v] = alt
                    self.prev[v] = u
                    heappush(self.Q, (alt, v))
 
 
    def shortest_distance(self, goal):
 
        return self.dist[goal]
 
    def shortest_path(self, goal):
 
        path = []
        vertice = goal
        while vertice is not None:
            path.append(vertice)
            vertice = self.prev[vertice]
 
        return path[::-1]