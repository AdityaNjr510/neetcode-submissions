# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, node):
        return 1 + max(self.depth(node.left), self.depth(node.right)) if node else 0

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        if abs(self.depth(root.left) - self.depth(root.right)) > 1:
            return False

        return True and self.isBalanced(root.left) and self.isBalanced(root.right)


        