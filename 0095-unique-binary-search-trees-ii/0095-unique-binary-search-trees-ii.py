# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n==0:return []
        def func(st,en):
            if st>en:return [None]
            ans = []
            for i in range(st,en+1):
                leftt = func(st,i-1)
                rightt = func(i+1,en)
                for l in leftt:
                    for r in rightt:
                        curr = TreeNode(i)
                        curr.left = l
                        curr.right = r
                        ans.append(curr)
            return ans
        return func(1,n)