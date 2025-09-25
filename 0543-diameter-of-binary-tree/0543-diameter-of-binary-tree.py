# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.diameter-1
    def height(self,root):
        if not root:return 0
        left = self.height(root.left)
        right = self.height(root.right)
        dia = left+right+1
        self.diameter = max(dia,self.diameter)
        return max(left,right)+1