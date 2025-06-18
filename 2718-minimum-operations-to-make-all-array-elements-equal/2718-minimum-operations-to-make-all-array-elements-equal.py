class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n=len(nums)
        nums.sort()
        ans = []
        pref = [*accumulate(nums, initial = 0)]
        for q in queries:
            i = bisect_left(nums,q)
            ans.append((q*i - pref[i])*2 + pref[-1] - q*n)
        return ans