class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def func(i,prev_diff):
            if i==n:
                return 0
            curr_diff = nums[i] - nums[i - 1]
            take = 0
            if (prev_diff >= 0 and curr_diff < 0) or (prev_diff <= 0 and curr_diff > 0):
                take = 1 + func(i + 1, curr_diff)
            
            not_take = func(i + 1, prev_diff)
            return max(take, not_take)
        if n<2:
            return n
        return 1 + func(1,0)