class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 1
        dp = [[1]*(k) for _ in range(n)]
        for i in range(n):
            for j in range(i):
                r = (nums[j]+nums[i]) % k
                l  = dp[j][r]+1
                dp[i][r] = max(dp[i][r],l)
                ans = max(ans,dp[i][r])
        return ans