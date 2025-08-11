class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp =  [[-1]*n for _ in range(n)]
        def func(i,j):
            if i==j:return 1
            if dp[i][j]!=-1:return dp[i][j]
            ans = float('inf')
            for k in range(i,j):
                ans = min(ans,func(i,k)+func(k+1,j))
            if s[i]==s[j]:ans-=1
            dp[i][j]=ans
            return ans
        return func(0,n-1)