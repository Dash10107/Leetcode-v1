# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def solve(head):
            s = ''
            if head:
                s+= str(head.val)
                if head.left or head.right:s+= '(' + solve(head.left)+')' 
                if head.right:s+= '('+solve(head.right)+')'
            return s
        return solve(root)