class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        n = len(grid);m = len(grid[0])
        dp = {};mod = 10**9+7
        def func(i,j,x):
            if i>=n or j>=m:return 0
            if i==n-1 and j==m-1:return (1 if x==k else 0)
            if (i,j,x) in dp:return dp[(i,j,x)]
            ways = 0
            if i+1<n:ways+=func(i+1,j,x^ grid[i+1][j])
            if j+1<m:ways+=func(i,j+1,x^ grid[i][j+1])
            dp[(i,j,x)]=(ways%mod)
            return ways%mod
        return func(0,0,grid[0][0])