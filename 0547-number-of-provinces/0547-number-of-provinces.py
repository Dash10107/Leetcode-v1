class Solution:
    def findCircleNum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        vis = set()
        
        def bfs(node):
            q = deque([node])
            vis.add(node)
            while q:
                cur = q.popleft()
                for nei in range(n):
                    if mat[cur][nei] == 1 and nei not in vis:
                        vis.add(nei)
                        q.append(nei)
        
        ans = 0
        for i in range(n):
            if i not in vis:
                ans += 1
                bfs(i)
        return ans
