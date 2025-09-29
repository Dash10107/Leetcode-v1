class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        div = nums[-1]
        ans = 0
        for i in range(n-2,-1,-1):
            if nums[i]>div:
                parts = (nums[i]+div-1)//div
                ans+= parts-1
                div = nums[i]//parts
            else:
                div=nums[i]
        return ans