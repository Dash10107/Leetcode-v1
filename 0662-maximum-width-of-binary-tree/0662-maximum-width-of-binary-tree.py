# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque([(root,0)])
        while q:
            l = len(q)
            _,first = q[0]
            for i in range(l):
                node,ind = q.popleft()
                ind = ind-first
                if node.left:
                    q.append((node.left,2*ind))
                if node.right:
                    q.append((node.right,2*ind + 1))
            if q:
                w = q[-1][1] - q[0][1] + 1
                ans = max(w,ans)
            else:
                ans = max(ans,1)
        return ans