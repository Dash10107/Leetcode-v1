class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        pref = 0
        best = [10**30]*k
        best[0] = 0
        ans = -10**30

        for i, x in enumerate(nums, 1):
            pref += x
            ans = max(ans, pref - best[i%k])
            best[i%k] = min(best[i%k], pref)

        return ans