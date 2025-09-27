# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        dic = {}
        childs = set()
        for p,c,l in descriptions:
            curr,child = None,None
            if p not in dic:curr=TreeNode(p)
            else:curr=dic[p]
            if c not in dic:child = TreeNode(c)
            else:                child = dic[c]
            if l:curr.left = child
            else:curr.right=child
            dic[p]=curr
            dic[c]=child
            childs.add(c)
        for p in dic:
            if p not in childs:return dic[p]
