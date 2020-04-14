class UnionFind():

    def __init__(self, N):
        self.__follow = [-1]*(N+1)
        self.__num_follower = [1]*(N+1)

    def root(self, a):
        r = a
        while self.__follow[r] > -1:
            r = self.__follow[r]
        return r
    
    def merge(self, a, b):
        ra = self.root(a)
        rb = self.root(b)
    
        if ra == rb:
            return
        
        if self.__num_follower[ra] < self.__num_follower[rb]:
            self.__follow[ra] = rb
            self.__follow[a] = rb
            self.__num_follower[rb] += self.__num_follower[ra]
        else:
            self.__follow[rb] = ra
            self.__follow[b] = ra
            self.__num_follower[ra] += self.__num_follower[rb]
    
    def issame(self, a, b):
        return self.root(a) == self.root(b)

    def size(self, a):
        return self.__num_follower(self.root(a))