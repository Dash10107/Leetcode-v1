# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def dfs(node,par,gpar):
            if not node:return
            if  gpar!=-1 and gpar.val%2==0:self.ans+=node.val
            dfs(node.left,node,par)
            dfs(node.right,node,par)
        dfs(root,-1,-1)
        return self.ans