# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        d = -1;ans=0;depth=0
        q = deque([root])
        curr = root
        while q:
            depth+=1
            n = len(q)
            while n:
                curr = q.popleft()
                if depth>d:
                    ans = curr.val
                    d = depth
                if curr.left:q.append(curr.left)
                if curr.right:q.append(curr.right)
                n-=1
        return ans