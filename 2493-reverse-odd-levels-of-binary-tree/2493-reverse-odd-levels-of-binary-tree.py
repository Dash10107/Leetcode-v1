# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.helper(root.left,root.right,0)
        return root

    def helper(self,leftN,rightN,level):
        if not leftN or not rightN:
            return 
        
        self.helper(leftN.left,rightN.right,level+1)
        self.helper(leftN.right,rightN.left,level+1)
        if level%2==0:
            leftN.val,rightN.val = rightN.val,leftN.val