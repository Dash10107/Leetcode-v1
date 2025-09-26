# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node,mav,miv):
            if node is None:
                return mav-miv
            mav =max(mav,node.val)
            miv = min(miv,node.val)
            left = dfs(node.left,mav,miv)
            right = dfs(node.right,mav,miv)
            return max(left,right)
        return dfs(root,float('-inf'),float('inf'))