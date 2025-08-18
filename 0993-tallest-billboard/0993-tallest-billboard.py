class Solution:
    def tallestBillboard(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def func(i,diff):
            if i==n:
                return 0 if diff==0 else float('-inf')
            ans = func(i+1,diff)
            ans = max(ans,func(i+1,diff-nums[i]))
            ans = max(ans,nums[i] + func(i+1,diff+nums[i])) 
            return ans
        return func(0,0)