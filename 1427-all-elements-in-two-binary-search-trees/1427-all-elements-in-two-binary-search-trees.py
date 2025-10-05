# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def dfs(node,vis):
            if node:
                dfs(node.left,vis)
                vis.append(node.val)
                dfs(node.right,vis)
        ans = []
        dfs(root1,ans)
        dfs(root2,ans)
        return sorted(ans)