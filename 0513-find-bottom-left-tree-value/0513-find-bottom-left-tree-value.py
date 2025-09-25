# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        d = -1;ans=0
        def dfs(head,depth):
            nonlocal d;nonlocal ans
            if not head:return
            if depth>d:
                d = depth
                ans = head.val
            dfs(head.left,depth+1)
            dfs(head.right,depth+1)
        dfs(root,0)
        return ans