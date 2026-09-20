# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findMinNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root is None:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: 
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
 
            minNode = self.findMinNode(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right,minNode.val)
        return root
        
        

        