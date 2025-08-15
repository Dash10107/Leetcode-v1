class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        mod = 10**9+7
        n = len(nums)
        dp = defaultdict(int)
        s  = defaultdict(int)
        for i in nums:
            dp[i]= ( dp[i]+1)%mod
            s[i]= ( s[i]+i)%mod
            dp[i]= (dp[i]+ dp[i-1]%mod)
            s[i]= (s[i]+ s[i-1]+(dp[i-1]*i)%mod)%mod
            dp[i]= (dp[i] + dp[i+1])%mod
            s[i]= (s[i] + s[i+1]+(dp[i+1]*i)%mod)%mod
        ans = 0
        for i in s:
            ans = (ans+s[i])%mod
        return ans