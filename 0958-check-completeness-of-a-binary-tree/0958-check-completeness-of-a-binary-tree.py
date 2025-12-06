# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:return True
        q = deque([root])
        none = False
        while q:
            node = q.popleft()
            if node is None:
                none = True
            else:
                if none:return False
                q.append(node.left)
                q.append(node.right)
        return True