# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q =deque([(root,None)])

        while q:
            n  = len(q)
            xp,yp=None,None
            for _ in range(n):
                node,par = q.popleft()
                if node.val==x:xp=par
                if node.val==y:yp=par
                if node.left:q.append((node.left,node))
                if node.right:q.append((node.right,node))
            if xp and yp:return xp!=yp
            if xp or yp:return False
        return False