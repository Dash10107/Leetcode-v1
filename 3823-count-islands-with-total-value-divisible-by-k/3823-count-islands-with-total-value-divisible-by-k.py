class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n,m = len(grid),len(grid[0])
        vis = [[False]*m for _ in range(n)]
        dirr = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(i,j):
            if vis[i][j]:
                return 0
            vis[i][j]=True
            c= grid[i][j]
            for dr,dc in dirr:
                nr,nc = i+dr,j+dc
                if 0<=nr<n and 0<=nc<m and not vis[nr][nc] and grid[nr][nc]!=0:
                    c+=dfs(nr,nc)
            return c
        ans =0
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0 and not vis[i][j]:
                    d = dfs(i,j)
                    if d%k==0:ans+=1

        return ans