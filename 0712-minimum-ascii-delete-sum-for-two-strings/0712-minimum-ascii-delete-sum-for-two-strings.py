class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def lcs(s,p):
            m,n = len(s),len(p)
            dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
            for i in range(m):
                for j in range(n):
                    if s[i]==p[j]:
                        dp[i+1][j+1] = dp[i][j]+ord(s[i])
                    else:
                        dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
                        
            return dp[-1][-1]
        
        common = lcs(s1,s2)
        total,res = 0,0
        for c in s1:
            total+=ord(c)
        for c in s2:
            total+=ord(c)
        
        res = total - common*2
        return res