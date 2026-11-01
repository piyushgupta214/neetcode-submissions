class UnionFind:

    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range (n):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, node):
        parentNode = self.parent[node]
        while parentNode != self.parent[parentNode]:
            self.parent[parentNode] = self.parent[self.parent[parentNode]]
            parentNode = self.parent[parentNode]
        return parentNode

    def union(self, a, b):
        parentA = self.find(a)
        parentB = self.find(b)

        if parentA == parentB:
            return False
        
        if self.rank[parentA] > self.rank[parentB]:
            self.parent[parentB] = parentA
        elif self.rank[parentB] > self.rank[parentA]:
            self.parent[parentA] = parentB
        else:
            self.parent[parentA] = parentB
            self.rank[parentB] += 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        uf = UnionFind(n)

        for edge in edges:
            uf.union(edge[0], edge[1])

        result = 0
        # print(uf.rank)
        for i in range(n):
            if uf.parent[i] == i:
                result += 1
        return result

        