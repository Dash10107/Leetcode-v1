class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n,m = len(s1),len(s2)
        dp = defaultdict(int)
        for i in range(n):
            dp[(i, -1)] = dp[(i-1, -1)] + ord(s1[i])
        for j in range(m):
            dp[(-1, j)] = dp[(-1, j-1)] + ord(s2[j])
        for i in range(n):
            t1 = ord(s1[i])
            for j in range(m):
                t2 = ord(s2[j])
                if s1[i]!=s2[j]:
                     dp[(i,j)]=min(dp[(i-1,j-1)]+t2+t1,dp[(i-1,j)]+t1,dp[(i,j-1)]+t2)
                else:
                    dp[(i,j)]=dp[(i-1,j-1)]
        return dp[(n-1,m-1)]