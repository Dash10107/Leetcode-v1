# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if node:
                l = dfs(node.left)
                r = dfs(node.right)
                self.ans+= abs(l)+abs(r)
                return node.val+l+r-1
            return 0
        s = dfs(root)
        return self.ans
