class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        copy = grid[:]
        def dfs(r,c):
            copy[r][c]=0
            ans = 1
            for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr,nc = r+dr,c+dc
                if 0<=nr<n and 0<=nc<m and copy[nr][nc]==1:
                    ans+= dfs(nr,nc)
            return ans
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    ans = max(ans,dfs(i,j))
        return ans

