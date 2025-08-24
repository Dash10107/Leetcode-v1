class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = defaultdict(lambda: defaultdict(int))
        ans = [0]*(k+1)
        for i in range(n):
            for rem in range(k,-1,-1):
                dp[nums[i]][rem]= max(dp[nums[i]][rem]+1,(ans[rem-1]+1 if rem>0 else 0))
                ans[rem]= max(ans[rem],dp[nums[i]][rem])
        return max(ans)