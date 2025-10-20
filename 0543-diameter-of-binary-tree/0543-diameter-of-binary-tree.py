# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def dia(node):
            if not node:return 0
            left = dia(node.left)
            right=dia(node.right)
            self.ans=max(self.ans,left+right+1)
            return max(left,right)+1
        temp = dia(root)
        return self.ans-1