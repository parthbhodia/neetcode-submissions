# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        #pass node along with boundaries
        def valid(node, left, right):
            #reaching null node means binary tree
            if not node:
                return True
            #basic BST algo for valid
            if not (node.val < right and node.val > left) : 
                return False


            return valid(node.left, left, node.val ) and valid(node.right, node.val, right)

        return valid(root, float("-inf"), float("inf"))