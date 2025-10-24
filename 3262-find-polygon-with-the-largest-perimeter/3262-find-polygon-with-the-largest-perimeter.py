class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        pref =nums[0]+nums[1]
        ans=-1
        for i in range(2,n):
            if pref>nums[i]:
                ans=max(ans,pref+nums[i])
            pref+=nums[i]
        return ans