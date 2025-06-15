"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:return node
        adj = {node.val:Node(node.val,[])}
        q = deque([node])
        while q:
            n = q.popleft()
            curr = adj[n.val]
            for neg in n.neighbors:
                if neg.val not in adj:
                    adj[neg.val]=Node(neg.val,[])
                    q.append(neg)
                curr.neighbors.append(adj[neg.val])
        return adj[node.val]