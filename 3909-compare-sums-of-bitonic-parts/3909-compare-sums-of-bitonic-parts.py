class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        n = len(nums)
        pref = 0
        for i in range(n-1):
            pref+=nums[i]
            if nums[i]>=nums[i+1]:
                break
        suff = sum(nums[i:])
        if pref>suff:return 0
        elif pref<suff:return 1
        else:return -1