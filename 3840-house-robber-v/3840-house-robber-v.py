class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n = len(nums)
        if n==0:return 0
        dp = [0]*n
        dp[0]=nums[0]
        for i in range(1,n):
            skip = dp[i-1]
            if colors[i]!=colors[i-1]:
                take =dp[i-1]+nums[i]
            else:
                take = nums[i] + (dp[i-2] if i>=2 else 0)
            dp[i]=max(take,skip)
        return dp[n-1]