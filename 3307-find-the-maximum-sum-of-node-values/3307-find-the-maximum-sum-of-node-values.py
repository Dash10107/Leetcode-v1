class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        @cache
        def f(i,c):
            if i==n:
                return float('-inf') if c==1 else 0
            return max(nums[i]+f(i+1,c),(nums[i]^k)+f(i+1,1-c))
        return f(0,0)