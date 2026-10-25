class Trie:

    def __init__(self):
        self.childs = {}
        self.word = False
    
    def addWord(self, word):
        curr = self
        for char in word:
            if char not in curr.childs:
                curr.childs[char] = Trie()
            
            curr = curr.childs[char]
        curr.word = True
        
    def search(self, word):
        curr = self
        for char in word:
            if char not in curr.childs:
                return False
            curr = curr.childs[char]
        return curr.word

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = Trie() 
        
        DIRECTIONS = [(0,1), (1,0),(0,-1),(-1,0)]
        visited = set()
        res = set()
        ROWS = len(board)
        COLS = len(board[0])
        # create a Trie for each word
        for word in words:
            root.addWord(word)

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or board[r][c] not in node.childs:
                return
            visited.add((r,c))
            node = node.childs[board[r][c]]
            word += board[r][c]
            if node.word:
                res.add(word)
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visited.remove((r,c))

        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, root, "")
        
        return list(res)
                


        