# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sums = defaultdict(int)
        def dfs(node):
            if not node:return 0
            left = dfs(node.left)
            right = dfs(node.right)
            sums[left+right+node.val]+=1
            return left+right+node.val
        res = dfs(root)
        mx = max(sums.values())
        return [s for s,c in sums.items() if c==mx]