# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 10**9+7
        alll = []
        def ts(node):
            if node is None:return 0
            s = node.val + ts(node.left)+ts(node.right)
            alll.append(s)
            return s
        s = ts(root)
        ans = 0
        for a in alll:
            ans = max(ans,a*(s-a))
        return ans%mod