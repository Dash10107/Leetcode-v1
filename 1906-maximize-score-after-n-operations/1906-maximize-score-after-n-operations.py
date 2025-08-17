class Solution:
    def maxScore(self, nums: List[int]) -> int:
        m = len(nums);n = m//2
        dp = [-1]*(1<<14)
        def func(op,mask):
            if op>n:return 0
            if dp[mask]!=-1:return dp[mask]
            for i in range(m):
                if (mask & 1<<i):continue
                for j in range(i+1,m):
                    if (mask & 1<<j):continue
                    new = mask | 1<<i | 1<<j
                    score = op* gcd(nums[i],nums[j]) + func(op+1, new )
                    dp[mask]= max(dp[mask],score)
            return dp[mask]
        return func(1,0)