class UnionFind:

    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}

        for i in range(1, n+1):
            self.parent[i] = i
            self.rank[i] = 0
        
    def find(self, n: int) -> int:
        parentNode = self.parent[n]
        while parentNode != self.parent[parentNode]:
            self.parent[parentNode] = self.parent[self.parent[parentNode]]
            parentNode = self.parent[parentNode]
        return parentNode
    
    def union(self, nodeA: int, nodeB: int) -> Bool:
        parentA = self.find(nodeA)
        parentB = self.find(nodeB)
        
        if parentA == parentB:
            return False

        if self.rank[parentA] > self.rank[parentB]:
            self.parent[parentB] = parentA
        elif self.rank[parentB] > self.rank[parentA]:
            self.parent[parentA] = parentB
        else:
            self.parent[parentA] = parentB
            self.rank[parentA] += 1

        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        unionFind = UnionFind(len(edges))
        res = []

        for edge in edges:
            if not unionFind.union(edge[0], edge[1]):
                res.append(edge)
        
        return res[-1]

        