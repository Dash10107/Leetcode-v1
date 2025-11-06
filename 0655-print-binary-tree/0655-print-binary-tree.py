# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get(root):
            if not root:return -1
            return 1+max(get(root.left),get(root.right))
        height = get(root)
        m = height+1
        n = 2**(height+1)-1
        tree = [['']*n for _ in range(m)]
        def dfs(curr,i,j):
            tree[i][j]=str(curr.val)
            if curr.left:
                dfs(curr.left,i+1,j-2**(height-i-1))
            if curr.right:
                dfs(curr.right,i+1,j+2**(height-i-1))
        dfs(root,0,(n-1)//2)
        return tree