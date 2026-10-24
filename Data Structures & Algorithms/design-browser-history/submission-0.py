class URLNode:

    def __init__(self, url, next=None, prev = None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = URLNode(homepage)
        self.current = self.home

    def visit(self, url: str) -> None:
        
        newNode = URLNode(url)
        newNode.prev = self.current
        self.current.next = newNode
        self.current = newNode

    def back(self, steps: int) -> str:
        
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        
        return self.current.url


    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        
        return self.current.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)