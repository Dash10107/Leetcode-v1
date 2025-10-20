# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.c=0;self.ans=0
        def dfs(node):
            if node is None:return 
            dfs(node.left)
            if self.c==k-1:
                self.ans=node.val
            self.c+=1
            dfs(node.right)
        dfs(root)
        return self.ans