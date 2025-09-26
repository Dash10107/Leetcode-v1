# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node,turn,l):
            if node is None:return 
            self.ans = max(self.ans,l)
            dfs(node.left,True,l+1 if not turn else 1)
            dfs(node.right,False,l+1 if turn else 1)
            return
        dfs(root,True,0)
        dfs(root,False,0)
        return self.ans