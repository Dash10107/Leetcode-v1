class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n=len(nums1);m=len(nums2)
        neg = float('-inf')
        dp = [[[neg]*(k+1) for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                dp[i][j][0]=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                for t in range(1,k+1):
                    dp[i][j][t]=max(dp[i][j][t],dp[i-1][j][t])
                    dp[i][j][t]=max(dp[i][j][t],dp[i][j-1][t])
                    dp[i][j][t]=max(dp[i][j][t],dp[i-1][j-1][t-1]+(nums1[i-1]*nums2[j-1]))
        # print(dp)
        return dp[n][m][k]