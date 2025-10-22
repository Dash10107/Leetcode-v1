class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid),len(grid[0])
        vis = [[False]*m for _ in range(n)]
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        cnt = 0
        def dfs(r,c):
            vis[r][c]=True
            for dr, dc in directions:
                nr = dr + r
                nc = dc+c
                if 0<=nr<n and 0<=nc<m and grid[nr][nc]=='1' and (not vis[nr][nc]):
                    vis[nr][nc]=True
                    dfs(nr,nc)
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1' and (not vis[i][j]):
                    cnt+=1
                    dfs(i,j)
        return cnt
