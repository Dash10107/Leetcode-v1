class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n=len(nums)
        s = sum(nums)
        f = sum(i*num for i,num in enumerate(nums))
        ans = f
        for i in range(1,n):
            f = f+ s- (n* nums[-i]) 
            ans = max(ans,f)
        return ans