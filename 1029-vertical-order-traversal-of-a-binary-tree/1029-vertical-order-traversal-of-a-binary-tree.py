# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []
        d = defaultdict()
        q = deque([(root,0,0)])
        while q:
            node,r,c = q.popleft()
            nodes.append((c,r,node.val))
            if node.left:
                q.append((node.left,r+1,c-1))
            if node.right:
                q.append((node.right,r+1,c+1))
        nodes.sort()
        ans = defaultdict(list)
        for c,r,v in nodes:
            ans[c].append(v)
        return [ans[x] for  x in sorted(ans)]