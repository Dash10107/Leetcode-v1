# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        def conv(node,parent):
            if not node:
                return
            if parent!=0:                graph[node.val].append(parent)
            if node.left:                graph[node.val].append(node.left.val)
            if node.right:                graph[node.val].append(node.right.val)
            conv(node.left,node.val)
            conv(node.right,node.val)
        conv(root,0)
        vis = set()
        q = deque([(start,0)])
        vis.add(start)
        ans = 0
        while q:
            node,lev = q.popleft()
            ans = lev
            for neg in graph[node]:
                if neg not in vis:
                    vis.add(neg)
                    q.append((neg,lev+1))
        return ans