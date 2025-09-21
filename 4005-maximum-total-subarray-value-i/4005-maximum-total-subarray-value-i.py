class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        m1,m2 = float('inf'),float('-inf')
        ans = 0
        for i in range(len(nums)):
            m1 = min(m1,nums[i])
            m2 = max(m2,nums[i])
            ans = max(ans,m2-m1)
        return ans*k