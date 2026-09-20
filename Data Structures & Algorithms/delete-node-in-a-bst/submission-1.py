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

         # BASE CASE:
        # If we reach an empty subtree, the key does not exist here.
        if root is None:
            return root


        # ---------------------------------------------------------
        # STEP 1: SEARCH FOR THE NODE
        # ---------------------------------------------------------

        # If key is smaller than the current node,
        # BST property tells us it can only be in the left subtree.
        if key < root.val:

            # Recursively delete the node from the left subtree.
            #
            # IMPORTANT:
            # We assign the returned subtree back to root.left
            # because deletion may change the root of that subtree.
            root.left = self.deleteNode(root.left, key)


        # If key is larger than the current node,
        # BST property tells us it can only be in the right subtree.
        elif key > root.val:

            # Recursively delete the node from the right subtree.
            #
            # Again, deletion may change the root of that subtree.
            root.right = self.deleteNode(root.right, key)


        # ---------------------------------------------------------
        # STEP 2: FOUND THE NODE TO DELETE
        # ---------------------------------------------------------

        # If key == root.val,
        # this is the node we need to delete.
        else:


            # -----------------------------------------------------
            # CASE 1:
            # Node has NO LEFT CHILD
            # -----------------------------------------------------

            if root.left is None:

                # Replace this node with its right child.
                #
                # This also handles a LEAF node because
                # root.right would also be None.
                return root.right


            # -----------------------------------------------------
            # CASE 2:
            # Node has NO RIGHT CHILD
            # -----------------------------------------------------

            elif root.right is None:

                # Replace this node with its left child.
                return root.left


            # -----------------------------------------------------
            # CASE 3:
            # Node has TWO CHILDREN
            # -----------------------------------------------------

            # We cannot simply remove this node because
            # both left and right subtrees must remain connected.
            #
            # So we find the INORDER SUCCESSOR:
            #
            # smallest node in the RIGHT subtree.
            minNode = self.findMinNode(root.right)


            # Copy the inorder successor's value into
            # the node we originally wanted to delete.
            #
            # Example:
            #
            #        5
            #       / \
            #      3   8
            #         / \
            #        6   9
            #
            # Delete 5.
            #
            # Minimum node in right subtree = 6.
            #
            # Replace:
            #
            #        5
            #
            # with:
            #
            #        6
            root.val = minNode.val


            # Now we have TWO copies of minNode.val:
            #
            # one at the current root
            # one inside the right subtree.
            #
            # Therefore, delete the original minimum node
            # from the right subtree.
            root.right = self.deleteNode(
                root.right,
                minNode.val
            )


        # Return the root of the possibly modified subtree.
        #
        # This is important because recursion reconnects
        # each modified subtree with its parent.
        return root
        
        

        