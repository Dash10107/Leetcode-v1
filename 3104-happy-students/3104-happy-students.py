class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort();ans = 0;n=len(nums)
        if 0<nums[0]:ans+=1
        for k in range(1,n):
            if nums[k-1]<k<nums[k]:
                ans+=1
        if nums[-1]<n:ans+=1
        return ans