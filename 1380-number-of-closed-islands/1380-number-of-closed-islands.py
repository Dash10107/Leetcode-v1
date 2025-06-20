class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        vis = [[False]*m for _ in range(n)]
        dirr = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(i,j):
            if vis[i][j]:
                return
            vis[i][j]=True
            for dr,dc in dirr:
                nr,nc = i+dr,j+dc
                if 0<=nr<n and 0<=nc<m and  grid[nr][nc]==0 and not vis[nr][nc]:
                    dfs(nr,nc)
        ans = 0
        for i in range(n):
            if grid[i][0] == 0 and not vis[i][0]:
                dfs(i, 0)
            if grid[i][m - 1] == 0 and not vis[i][m - 1]:
                dfs(i, m - 1)

        for j in range(m):
            if grid[0][j] == 0 and not vis[0][j]:
                dfs(0, j)
            if grid[n - 1][j] == 0 and not vis[n - 1][j]:
                dfs(n - 1, j)
        

        for i in range(1,n-1):
            for j in range(1,m-1):
                if grid[i][j]==0 and not vis[i][j]:
                    dfs(i,j)
                    ans+=1
        return ans