class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0
    
    def traverseList(self, index):
        temp = self.head
        while index > 0:
            temp = temp.next
            index -= 1

        return temp

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        temp = self.traverseList(index+1)
        return temp.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None: 
        self.addAtIndex(self.size, val) 

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        if index < 0:
            index = 0 

        temp = self.traverseList(index)

        newNode = ListNode(val)
        newNode.next = temp.next
        newNode.prev = temp
        if temp.next:
            temp.next.prev = newNode
        temp.next = newNode

        self.size += 1

    
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        temp = self.traverseList(index)

        nodeToDelete = temp.next
        temp.next = nodeToDelete.next

        if nodeToDelete.next:
            nodeToDelete.next.prev = temp

        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)