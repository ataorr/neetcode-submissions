# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        result = []
        while queue:
            length = len(queue)
            right = None
            for i in range(length):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    right = node
            if right:
                result.append(right.val)
        return result            
            
