class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid);m=len(grid[0])
        rows = [0]*n;cols=[0]*m
        for i in range(n):
            for j in range(m):
                rows[i]=max(rows[i],grid[i][j])
                cols[j]=max(cols[j],grid[i][j])
        ans = 0
        for i in range(n):
            for j in range(m):
                mi = min(rows[i],cols[j])
                ans+=mi-(grid[i][j])
        return ans


