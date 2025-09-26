# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = '~'
        def dfs(node,s):
            if node:
                s += chr(node.val + ord('a'))
                if node.left is None and node.right is None:
                    self.ans = min(self.ans,s[::-1])
                dfs(node.left,s)
                dfs(node.right,s)
                s = s[:-1]
            return
        dfs(root,'')
        return self.ans