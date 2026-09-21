# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None
        self.inorder(root)
        return self.result

    
    def inorder(self, root: Optional[TreeNode]) -> None:
        if not root or self.result is not None:
            return
        
        # 1. Traverse left
        self.inorder(root.left)
        
        # 2. Process current node
        self.k -= 1
        if self.k == 0:
            self.result = root.val
            return
        
        # 3. Traverse right
        self.inorder(root.right)

