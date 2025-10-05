"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:return []
        levels = []
        q = deque([root])
        while q:
            n = len(q)
            curr = []
            for _ in range(n):
                node = q.popleft()
                if node and node.children:
                    q.extend(node.children)
                curr.append(node.val)
            levels.append(curr)
        return levels
