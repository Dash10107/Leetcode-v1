class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        ans = 0;n=len(nums)
        start = nums[-1];avgg=start
        for i in range(n-2,-1,-1):
            if nums[i]>avgg:ans+=1
            start+=nums[i]
            avgg = start//(n-i)
        return ans