# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans = 0
        def func(r):
            if not r:
                return (0,0)
            ls,ln = func(r.left)
            rs,rn = func(r.right)
            ts = ls+rs+r.val
            tn = ln+rn+1
            if r.val == ts//tn:
                self.ans+=1
            return (ts,tn)
        func(root)
        return self.ans