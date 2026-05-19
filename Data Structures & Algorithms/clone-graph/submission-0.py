"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodemap = {}
        if not node:
            return None
        
        def bfs(node):
            q = deque()
            nodemap[node] = Node(node.val)
            q.append(node)
            while q:
                cur = q.popleft()
                for n in cur.neighbors:
                    if n not in nodemap:
                        nodemap[n] = Node(n.val)
                        q.append(n)
                    nodemap[cur].neighbors.append(nodemap[n])
        bfs(node)
        return nodemap[node]