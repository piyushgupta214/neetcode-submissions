class UnionFind:

    def __init__(self, n):
        self.parents = {}
        self.ranks = {}

        for i in range(n):
            self.parents[i] = i
            self.ranks[i] = 0
    
    def find(self, n):
        while n != self.parents[n]:
            self.parents[n] = self.parents[self.parents[n]]
            n = self.parents[n]
        return n
    
    def union(self, a, b):
        parentA = self.find(a)
        parentB = self.find(b)

        if parentA == parentB:
            return False
        
        if self.ranks[parentA] > self.ranks[parentB]:
            self.parents[parentB] = parentA
        elif self.ranks[parentB] > self.ranks[parentA]:
            self.parents[parentA] = parentB
        else:
            self.parents[parentA] = parentB
            self.ranks[parentB] += 1
        
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        result = []
        uf = UnionFind(len(accounts))
        emailToAccount = {} # email -> index of account

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAccount:
                    uf.union(i, emailToAccount[email])
                else:
                    emailToAccount[email] = i

        
        emailGroup = defaultdict(list)  # index of acc -> list of emails
        
        for e, i in emailToAccount.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)
        
        
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            result.append([name] + sorted(emailGroup[i]))
        
        return result

        