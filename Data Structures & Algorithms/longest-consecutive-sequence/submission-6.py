class UnionFind:

    def __init__(self, nums: List[int]):
        self.parents = {}
        self.ranks = {}

        for num in nums:
            self.parents[num] = num
            self.ranks[num] = 0
    
    def find(self, num):
        parentNode = self.parents[num]
        while parentNode != self.parents[parentNode]:
            self.parents[parentNode] = self.parents[self.parents[parentNode]]
            parentNode = self.parents[parentNode]
        return parentNode
    
    def union(self, numA, numB):
        parentA = self.find(numA)
        parentB = self.find(numB)

        if parentA == parentB:
            return False
        
        if self.ranks[parentA] > self.ranks[parentB]:
            self.parents[parentB] = parentA
        elif self.ranks[parentB] > self.ranks[parentA]:
            self.parents[parentA] = parentB
        else:
            self.parents[parentA] = parentB
            self.ranks[parentB] += 1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        uf = UnionFind(nums)
        numSet = set(nums)
        for num in nums:
            if num+1 in numSet:
                uf.union(num, num+1)

        counts = defaultdict(int)

        for num in numSet:
            root = uf.find(num)
            counts[root] += 1
        
        return max(counts.values())
        