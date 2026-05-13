"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodedict = collections.defaultdict(lambda: Node(0))
        nodedict[None] = None

        cur = head
        while cur:
            nodedict[cur].val = cur.val
            nodedict[cur].next = nodedict[cur.next]
            nodedict[cur].random = nodedict[cur.random]
            cur = cur.next
            
        return nodedict[head]