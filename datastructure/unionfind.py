class UnionFind:

    def __init__(self, N):
        self.follow = [-1]*(N+1)
        self.num_follower = [1]*(N+1)

    def root_index_of(self, a):
        r = a
        while self.follow[r] > -1:
            r = self.follow[r]
        return r
    
    def connet(self, a, b):
        ra = self.root_index_of(a)
        rb = self.root_index_of(b)
    
        if ra == rb:
            return
        
        if self.num_follower[ra] < self.num_follower[rb]:
            self.follow[ra] = rb
            self.follow[a] = rb
            self.num_follower[rb] += self.num_follower[ra]
        else:
            self.follow[rb] = ra
            self.follow[b] = ra
            self.num_follower[ra] += self.num_follower[rb]
    
    def conneted(self, a, b):
        return self.root_index_of(a) == self.root_index_of(b)