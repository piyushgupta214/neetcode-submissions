class Trie:

    def __init__(self):
        self.word = False
        self.childs = {}

class WordDictionary:

    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.childs:
                curr.childs[c] = Trie()
            curr = curr.childs[c]
        curr.word = True

    def search(self, word: str) -> bool:

        def dfs(index, root):
            curr = root
            for i in range(index, len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.childs.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.childs:
                        return False
                    curr = curr.childs[c]
            return curr.word
        return dfs(0, self.root)