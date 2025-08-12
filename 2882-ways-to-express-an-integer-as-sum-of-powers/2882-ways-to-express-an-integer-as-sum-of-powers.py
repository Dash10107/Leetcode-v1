class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9+7
        powers = [];i=1
        while (p:= i**x)<=n:
            powers.append(p)
            i+=1
        dp = [0]*(n+1)
        dp[0]=1
        for p in powers:
            for t in range(n,p-1,-1):
                dp[t]= (dp[t]+dp[t-p])%mod
        return dp[n]