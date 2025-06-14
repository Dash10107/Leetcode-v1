class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n,m = len(nums1),len(nums2)
        dp = defaultdict(int)
        for i in range(n):
            for j in range(m):
                dp[i,j]= max(dp[i-1,j-1]+(nums1[i]==nums2[j]),dp[i-1,j],dp[i,j-1])
        return dp[n-1,m-1]