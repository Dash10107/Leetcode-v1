class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+ nums + [1]
        n = len(nums)
        ans = 0
        dp = [[0]*n for _ in range(n)]
        for le in range(2,n):
            for left in range(n-le):
                right= left+le
                for i in range(left+1,right):
                    coins = nums[left]*nums[right]*nums[i]
                    dp[left][right] = max(dp[left][right],coins+dp[left][i]+dp[i][right])
        return dp[0][n-1]
