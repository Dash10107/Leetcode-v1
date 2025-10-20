# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(r1,r2):
            if not r1 and not r2:return True
            if (r1 and not r2) or (r2 and not r1) or (r1.val!=r2.val):return False
            left = check(r1.left,r2.right)
            right = check(r1.right,r2.left)
            return left and right
        if not root:return True
        return check(root.left,root.right)