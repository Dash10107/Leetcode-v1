class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1 
        i = 0
        minSoFar = nums[0]
        while i<len(nums):
            if nums[i]-minSoFar>k:
                ans+=1
                minSoFar = nums[i]
            i+=1
        return ans
                