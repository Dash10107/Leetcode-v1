class Solution:
    def numSubmat(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*m for i in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    continue
                dp[i][j]= dp[i][j-1]+1 if j>0 else 1
                width = dp[i][j]
                for k in range(i,-1,-1):
                    width = min(width,dp[k][j])
                    if width==0:break
                    ans+= width
        return ans