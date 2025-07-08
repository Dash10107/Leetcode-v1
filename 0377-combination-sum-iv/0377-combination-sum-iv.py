class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def func(s):
            if s==target:
                return 1
            if s>target:
                return 0
            c = 0
            for i in nums:
                c+= func(s+i)
            return c
        return func(0)