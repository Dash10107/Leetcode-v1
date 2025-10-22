class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        def dfs(r, c):
            grid[r][c] = '0'  # mark visited
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '1':
                    dfs(nr, nc)

        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j)
        return cnt
