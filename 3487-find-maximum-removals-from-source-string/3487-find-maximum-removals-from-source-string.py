class Solution:
    def maxRemovals(self, source: str, pattern: str, target: List[int]) -> int:
        n = len(source);m=len(pattern)
        s = set(target)
        dp = [[float('-inf')]*(m+1) for _ in range(n+1)]
        dp[n][m]=0
        for i in range(n-1,-1,-1):
            for j in range(m,-1,-1):
                if j==m:dp[i][j]= int(i in s)+dp[i+1][j]
                else:
                    dp[i][j]= int(i in s)+dp[i+1][j]
                    if source[i]==pattern[j]:
                        dp[i][j]=max(dp[i][j],dp[i+1][j+1])
        return (dp[0][0] if dp[0][0]!=float('-inf') else 0)