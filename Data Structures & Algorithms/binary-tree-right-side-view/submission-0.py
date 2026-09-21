# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        result = []

       # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        result = []

        if root:
            queue.append(root)

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.pop(0)
                
                # If 'i' is the last index of the current level,
                # this node is guaranteed to be the rightmost visible node.
                if i == level_length - 1:
                    result.append(node.val)
                
                # Always add left first, then right, so the rightmost node 
                # naturally lands at the end of the next level's queue.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

        