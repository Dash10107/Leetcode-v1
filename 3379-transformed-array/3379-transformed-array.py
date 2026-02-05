class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = nums[:]
        if n <=1:
            return nums
        for i in range(n):
            if nums[i]>0:
                right = i + nums[i]
                if right>=n:
                    right%=n
                res[i]=nums[right]
            elif nums[i]<0:
                left = i - abs(nums[i])
                while left<0:
                    left+=n
                res[i]=nums[left]
            else:
                res[i]=nums[i]    
            
        return res