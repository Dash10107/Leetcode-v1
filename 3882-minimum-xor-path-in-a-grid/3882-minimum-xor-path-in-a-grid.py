class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n=len(grid);m=len(grid[0])
        x = 1024
        dp = [[[0]*x for j in range(m)] for i in range(n)]
        dp[0][0][grid[0][0]]=1
        for i in range(n):
            for j in range(m):
                for k in range(x):
                    xk = k^grid[i][j]
                    if i and dp[i-1][j][xk]:
                        dp[i][j][k]=1
                    if j and dp[i][j-1][xk]:
                        dp[i][j][k]=1
        ans = 0
        while ans<k:
            if dp[-1][-1][ans]:
                break
            ans+=1
        return ans 