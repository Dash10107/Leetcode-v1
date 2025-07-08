class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def func(s,e):
            if s==e:
                return nums[s]
            pick = nums[s]-func(s+1,e)
            pickend = nums[e] - func(s,e-1)
            return max(pick,pickend)
        return func(0,len(nums)-1)>=0