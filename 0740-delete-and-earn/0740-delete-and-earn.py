class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        freq = [0]*(max(nums)+1)
        for ni in nums:
            freq[ni]+=ni
        size = len(freq)
        if size <= 2:
            return max(freq)
        dp = [0] * len(freq)
        dp[1] = freq[1]
        for i in range(2,len(freq)):
            dp[i]=max(freq[i]+dp[i-2],dp[i-1])
        return dp[len(freq)-1]