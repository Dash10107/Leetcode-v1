class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        k = len(nums1)
        n = 1<<k
        dp = [float('inf')]*n
        dp[n-1]=0
        for mask in range(n-1,-1,-1):
            i = bin(mask).count('1')
            if i==k:continue
            for j in range(k):
                if not (mask & 1<<j):
                    new = mask | (1<<j)
                    cost = (nums1[i]^nums2[j]) + dp[new]
                    dp[mask]=min(dp[mask],cost)
        return dp[0]
