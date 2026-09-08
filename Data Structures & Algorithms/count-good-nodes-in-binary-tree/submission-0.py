# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):

            if not node:
                return 0
            #check if the node is a good node or not
            res = 1 if node.val >= maxVal else 0
            #update the max value
            maxVal = max(maxVal, node.val)
            #count and update the number in the res
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            
            return res
        
        return dfs(root, root.val)