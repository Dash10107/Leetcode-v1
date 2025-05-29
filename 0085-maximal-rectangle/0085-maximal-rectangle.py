class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[(0,0)]*m for i in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=='0':
                    continue
                left = top = 1
                if i-1>=0:left += dp[i-1][j][1]
                if j-1>=0:top += dp[i][j-1][0]
                dp[i][j]=(top,left)
                temp = top
                for k in range(i,i-left,-1):
                    temp = min(temp,dp[k][j][0])
                    area = temp * (i-k+1)
                    ans = max(area,ans)
        return ans                