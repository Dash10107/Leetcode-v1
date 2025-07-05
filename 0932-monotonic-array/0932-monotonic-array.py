class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        f = True
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                f = False

        if f:
            return f
        else:
            f = True
            for i in range(1,len(nums)):
                if nums[i]>nums[i-1]:
                    f = False
            return f