class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        n = len(nums);ans=0
        m = 0;left=[0]*n;right=[0]*n
        for i in range(n):
            left[i]=m
            m = max(m,nums[i])
        m=0
        for i in range(n-1,-1,-1):
            right[i]=m
            m = max(m,nums[i])
            
        for i in range(n):
            if left[i]>nums[i] and right[i]>nums[i]:
                ans+=1
        return ans