# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getDirections(self, root: Optional[TreeNode], start: int, desti: int) -> str:
        def dfs(node,targ,path):
            if not node:return False
            if node.val==targ:return True
            path.append('L')
            if dfs(node.left,targ,path):return True
            path.pop()
            path.append('R')
            if dfs(node.right,targ,path):return True
            path.pop()
            return False
        st,dest = [],[]
        dfs(root,start,st)
        dfs(root,desti,dest)
        com = 0
        while com<len(st) and com<len(dest) and st[com]==dest[com]:
            com+=1
        dirr = 'U'*(len(st)-com)+ ''.join(dest[com:])
        return dirr