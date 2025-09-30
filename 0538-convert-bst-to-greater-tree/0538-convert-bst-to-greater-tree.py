# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node,curr):
            if not node:return curr
            curr=dfs(node.right,curr)
            node.val = node.val+curr
            curr = node.val
            curr = dfs(node.left,curr)
            return curr
        dfs(root,0)
        return root