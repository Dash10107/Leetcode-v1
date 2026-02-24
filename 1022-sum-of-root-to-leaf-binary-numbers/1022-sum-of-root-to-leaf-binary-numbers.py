# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node,curr):
            if node:
                if not node.left and not node.right:
                    curr+=str(node.val)
                    self.ans+=int(curr,2)
                dfs(node.left,curr+str(node.val))
                dfs(node.right,curr+str(node.val))
        dfs(root,'')
        return self.ans
