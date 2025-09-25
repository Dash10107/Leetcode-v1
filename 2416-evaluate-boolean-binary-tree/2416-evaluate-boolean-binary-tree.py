# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(head):
            ans = False
            if head:
                left = dfs(head.left)
                right = dfs(head.right)
                if head.val == 2:
                    ans = left or right
                elif head.val ==3:
                    ans = left and right
                else:
                    ans = True if head.val ==1 else False
            return ans
        return dfs(root)