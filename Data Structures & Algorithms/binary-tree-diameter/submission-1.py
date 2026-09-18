# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def length(self, node):
        return 1 + max(self.length(node.left), self.length(node.right)) if node else 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        dia = self.length(root.left) + self.length(root.right)

        return max(dia, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))