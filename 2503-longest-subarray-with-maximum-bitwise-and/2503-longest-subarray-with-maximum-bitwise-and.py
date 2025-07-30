class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        ans = 1;j=0
        while j<len(nums):
            c=0
            while j<len(nums) and nums[j]==m:
                c+=1
                j+=1
            else:
                j+=1
            ans = max(ans,c)
        return ans 