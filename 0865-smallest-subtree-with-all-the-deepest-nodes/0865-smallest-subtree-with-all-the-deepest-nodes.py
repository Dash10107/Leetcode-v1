# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
            depth = {None:-1}
            def dfs(node,par=None):
                if node:
                    depth[node]=depth[par]+1
                    dfs(node.left,node)
                    dfs(node.right,node)
            dfs(root)
            temp = max(depth.values())
            def answer(root):
                if not root or depth.get(root,None)==temp:
                    return root
                left,right = answer(root.left),answer(root.right)
                return root if left and right else left or right
            return answer(root)