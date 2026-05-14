# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.result = True
        def dfs(p, q):
            if not p and not q:
                return None
            elif p and q and p.val == q.val:
                dfs(p.left, q.left)
                dfs(p.right, q.right)
            else:
                self.result = False
        dfs(p, q)
        return self.result