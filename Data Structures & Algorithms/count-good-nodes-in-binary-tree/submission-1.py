# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0
        if not root:
            return self.result
        def dfs(root, maxNum):
            if not root:
                return
            if root.val >= maxNum:
                self.result += 1
                print(root.val)
            maxNum = max(root.val, maxNum)
            dfs(root.left, maxNum)
            dfs(root.right, maxNum)
        dfs(root, root.val)
        return self.result