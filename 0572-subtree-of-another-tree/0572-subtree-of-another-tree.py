# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(r,sr,match):
            if not sr and not r:return True
            if not r or not sr:return False
            if r.val==sr.val:
                if dfs(r.left,sr.left,True) and dfs(r.right,sr.right,True):return True
            if match:return False
            return dfs(r.left,sr,False) or dfs(r.right,sr,False)
        return dfs(root,subRoot,False)
