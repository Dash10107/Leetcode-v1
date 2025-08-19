class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        i=0;n=len(nums)
        ans = 0
        while i<n:
            j = i+1
            while j<n and nums[j]>nums[j-1]:
                j+=1
            ans = max(ans,j-i)
            i=j
        return ans