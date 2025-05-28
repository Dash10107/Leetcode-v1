class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*m for i in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=='0':
                    continue
                left = top= diag = 0
                if i-1>=0:left = dp[i-1][j]
                if j-1>=0:top = dp[i][j-1]
                if (i-1>=0 and j-1>=0):diag = dp[i-1][j-1]
                dp[i][j] = min([left,top,diag])+1
                ans = max(ans,dp[i][j])
        return (ans*ans)