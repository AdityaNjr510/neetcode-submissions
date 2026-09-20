# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        def good(node, maxm):
            if not node:
                return 0

            left = good(node.left, max(node.val, maxm))
            right = good(node.right , max(node.val, maxm))
            
            if node.val >= maxm:                
                return 1 + left + right
            else:
                return left + right

        return good(root, float('-inf'))

        

        