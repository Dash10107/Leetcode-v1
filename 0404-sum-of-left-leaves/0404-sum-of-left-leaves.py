# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(head):
            s = 0
            if head:
                if head.left and head.left.left is None and head.left.right is None:
                    s+=head.left.val
                s+=dfs(head.left)
                s+=dfs(head.right)
            return s
        return dfs(root)