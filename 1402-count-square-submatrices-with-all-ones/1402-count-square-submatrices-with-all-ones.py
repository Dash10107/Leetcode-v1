class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        n = len(mat);m=len(mat[0])
        dp = [[0]*m for i in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:continue
                left=right=diag=0
                if i-1>=0:left=dp[i-1][j]
                if j-1>=0:right = dp[i][j-1]
                if (i-1>=0 and j-1>=0):diag = dp[i-1][j-1]
                dp[i][j]= min(left,right,diag)+mat[i][j]
                ans+= dp[i][j]
        return ans