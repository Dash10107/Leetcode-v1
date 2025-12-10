class Solution:
    def countPermutations(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if nums[i]<=nums[0]:
                return 0
        ans = 1
        mod = int(10**9+7)
        for i in range(2,len(nums)):
            ans *= (i%mod)
        return ans%mod