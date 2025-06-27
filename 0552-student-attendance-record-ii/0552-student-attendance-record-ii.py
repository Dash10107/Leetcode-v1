class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9+7
        dp=[[[-1]*3 for _ in range(2)] for _ in range(n+1)]
        def f(ni,ab,la):
            if ni==0:
                return 1
            if dp[ni][ab][la]!=-1:
                return dp[ni][ab][la]
            ans = 0
            ans+= f(ni-1,ab,0)
            if ab<1:
                ans+= f(ni-1,ab+1,0)
            if la<2:
                ans+= f(ni-1,ab,la+1)
            dp[ni][ab][la]=ans
            return ans%mod
        return f(n,0,0)