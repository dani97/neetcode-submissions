class UnionFind:
    def __init__(self, size: int):
        self.rank = [1] * size
        self.root = [i for i in range(size)]
        self.count = size
    
    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
               self.root[root_y] = root_x
            elif self.rank[root_y] < self.rank[root_x]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1

    def getCount(self) -> int:
        return self.count

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = max(edges, key = lambda x: x[1])
        uf = UnionFind(N[1])

        previousCount = N
        for index, edge in enumerate(edges):
            uf.union(edge[0] - 1, edge[1] - 1)
            if uf.getCount() == previousCount:
                return edges[index]
            previousCount = uf.getCount()
        return []
