class TreeNode:

    def __init__(self):
        self.childern = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.childern:
                curr.childern[c] = TreeNode()
            curr = curr.childern[c]
        curr.word = True


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.childern:
                return False
            curr = curr.childern[c]
        
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.childern:
                return False
            curr = curr.childern[c]
        
        return True
        