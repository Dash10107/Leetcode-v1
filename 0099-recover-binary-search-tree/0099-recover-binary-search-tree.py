# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first,sec=None,None
        prev=None
        def dfs(node):
            nonlocal first,sec,prev
            if node is None:return
            dfs(node.left)
            if prev and prev.val>node.val:
                if not first:first=prev
                sec=node
            prev=node
            dfs(node.right)
        dfs(root)
        temp = first.val
        first.val=sec.val;sec.val=temp
        """
        Do not return anything, modify root in-place instead.
        """
        