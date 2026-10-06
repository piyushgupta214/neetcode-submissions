# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        delta = targetSum
        return self.calculateSum(root, delta)

    def calculateSum(self, root: Optional[TreeNode], delta: int) -> bool:

        if not root:
            return False
        
        delta = delta - root.val

        if not root.left and not root.right:
            return delta == 0
        
        if self.calculateSum(root.left, delta):
            return True
        if self.calculateSum(root.right, delta):
            return True
       
        return False

        