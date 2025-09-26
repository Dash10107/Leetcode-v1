# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0
        while q:
            n = len(q)
            if level%2==0:
                m = float('-inf')
                for _ in range(n):
                    node = q.popleft()
                    if node.val%2==1 and node.val>m :
                        if node.left:q.append(node.left)
                        if node.right:q.append(node.right)
                        m = node.val
                    else:
                        return False
            else:
                m = float('inf')
                for _ in range(n):
                    node = q.popleft()
                    if node.val%2==0 and node.val<m:
                        if node.left:q.append(node.left)
                        if node.right:q.append(node.right)
                        m = node.val
                    else:
                        return False
            level+=1
        return True