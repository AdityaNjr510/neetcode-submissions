# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, minm, maxm):
            if not node:
                return True
            if node.val <= minm or node.val >= maxm:
                return False

            left = dfs(node.left, minm, min(node.val, maxm))
            right = dfs(node.right, max(node.val, minm), maxm)
            return left and right

        return dfs(root, float('-inf'), float('inf'))

