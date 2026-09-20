# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = collections.deque()
        if not root:
            return []
        q.append(root)
        res = []

        while q:
            qlen = len(q)

            sub_res = []
            for _ in range(qlen):
                node = q.popleft()
                sub_res.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(sub_res)

        return res
            