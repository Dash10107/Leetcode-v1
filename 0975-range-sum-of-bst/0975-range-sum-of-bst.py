# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(head):
            ans=0
            if head:
                ans+=dfs(head.left)
                ans+=dfs(head.right)
                if low<=head.val<=high:
                    ans+=head.val
            return ans
        return dfs(root) 