# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrder = []
        self.inorder(root, inOrder)
        return inOrder[k-1]

    def inorder(self, root: Optional[TreeNode], inOrder: [int] ):

        if not root:
            return

        self.inorder(root.left, inOrder)
        inOrder.append(root.val)
        self.inorder(root.right, inOrder)

