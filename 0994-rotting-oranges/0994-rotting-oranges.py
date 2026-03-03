class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        vis = [[0]*m for _ in range(n)]
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                        q.append((i,j))
                        vis[i][j]=2
                else:
                    vis[i][j]=0
        ans = 0;l=0
        while q:
            nn = len(q)
            for _ in range(nn):
                u,v = q.popleft()
                ans = max(ans,l)
                for dr, dc in directions:
                    nr = dr+u;nc = dc+v
                    if 0<=nr<n and 0<=nc<m and vis[nr][nc]!=2 and grid[nr][nc]==1:
                        q.append((nr,nc))
                        vis[nr][nc]=2
            if q:
                l+=1
        for i in range(n):
            for j in range(m):
                if vis[i][j]!=2 and grid[i][j]==1:
                    return -1
        return l