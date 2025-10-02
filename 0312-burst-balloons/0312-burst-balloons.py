class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+ nums + [1]
        n = len(nums)
        ans = 0
        @cache
        def func(left,right):
            if right-left<=1:return 0
            ans = 0
            for i in range(left+1,right):
                coins = nums[left]*nums[right]*nums[i]
                l = func(left,i)
                r = func(i,right)
                ans = max(ans,coins+l+r)
            return ans
        return func(0,n-1)
