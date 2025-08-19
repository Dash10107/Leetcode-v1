class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0;i=0;n=len(nums);curr=0
        while i<n:
            if nums[i]==0:
                curr+=1
                ans+=curr
            else:
                curr=0
            i+=1
        return ans