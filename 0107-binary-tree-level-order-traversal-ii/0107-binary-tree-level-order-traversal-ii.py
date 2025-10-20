# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels=[]
        q=deque([root])
        if not root:return []
        while q:
            n = len(q)
            temp = []
            for _ in range(n):
              node = q.popleft()
              if node:
                temp.append(node.val)
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
            levels.append(temp)
        return levels[::-1]