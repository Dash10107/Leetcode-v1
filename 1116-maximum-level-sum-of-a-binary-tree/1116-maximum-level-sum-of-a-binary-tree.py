# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level=1
        ans = float('-inf');main=0
        q = deque([root])
        while q:
            n = len(q)
            temp = 0
            for _ in range(n):
                node = q.popleft()
                temp+=node.val
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
            if temp>ans:
                ans=temp
                main=level
            level+=1
        return main