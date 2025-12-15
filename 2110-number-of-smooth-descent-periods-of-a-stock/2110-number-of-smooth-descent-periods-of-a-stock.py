class Solution:
    def getDescentPeriods(self, nums: List[int]) -> int:
        ans = 1;i=1;n=len(nums);curr=1
        while i<n:
            if nums[i]+1==nums[i-1]:
                curr+=1
                ans+=curr
            else:
                curr=1
                ans+=curr
            i+=1
        return ans