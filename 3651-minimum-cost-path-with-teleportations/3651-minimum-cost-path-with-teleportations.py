class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        n,m = len(grid),len(grid[0])
        cells = [(i,j) for i in range(n) for j in range(m)]
        cells.sort( key=lambda x:grid[x[0]][x[1]])
        dp = [[float('inf')] * m for _ in range(n)]
        for _ in range(k+1):
            best = float('inf')
            st = 0
            for i in range(len(cells)):
                r,c = cells[i]
                best = min(best,dp[r][c])
                if i+1<len(cells) and grid[r][c]==grid[cells[i+1][0]][cells[i+1][1]]:
                    continue
                for g in range(st,i+1):
                    gr,gc = cells[g]
                    dp[gr][gc]=best
                st=i+1
            for i in range(n-1,-1,-1):
                for j in range(m-1,-1,-1):
                    if i==n-1 and j==m-1:
                        dp[i][j]=0
                        continue
                    if i+1<n:
                        dp[i][j]= min(dp[i][j],dp[i+1][j]+grid[i+1][j])
                    if j+1<m:
                        dp[i][j]= min(dp[i][j],dp[i][j+1]+grid[i][j+1])
        return dp[0][0]