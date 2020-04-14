#ABC079D Wall

#例題の実装
class WarshallFloyd:
    def __init__(self, n):
        self.n = n
        self.dist = [[float("inf")]*(n+1) for _ in range(n+1)]
 
    def add_edge(self, a, b, weight):
        self.dist[a][b] = weight
 
    def make_short_path(self):
        for i in range(self.n+1):
            for j in range(self.n+1):
                for k in range(self.n+1):
                    self.dist[i][j] = min(self.dist[i][j], \
                    self.dist[i][k] + self.dist[k][j])
 
    def shortest_distance(self, start, goal):
        return self.dist[start][goal]
 
h, w = map(int, input().split())
w = WarshallFloyd(10)
for i in range(10):
    power = list(map(int, input().split()))
    for j in range(10):
        w.add_edge(i, j, power[j])
 
#最小経路を求める
w.make_short_path()
ans = 0
for i in range(h):
    wall = list(map(int, input().split()))
    for item in wall:
        if item >= 0:
            ans += w.shortest_distance(item, 1)
 
print(ans)
