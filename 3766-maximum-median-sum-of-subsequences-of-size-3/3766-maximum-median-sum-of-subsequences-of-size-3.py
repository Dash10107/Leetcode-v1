class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans=0;i=0;j=n-1
        while i<j:
            s = nums[i];t = nums[j];u = nums[j-1]
            ans+=u
            j-=2
            i+=1
        return ans