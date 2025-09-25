# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(head):
            ans = []
            if head:
                ans+= dfs(head.left)
                ans+=dfs(head.right)
                if head.left is None and head.right is None:
                    ans.append(head.val)
            return ans
        return dfs(root1)==dfs(root2)