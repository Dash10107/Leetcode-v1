class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        @lru_cache(None)
        def func(i):
            if i==n:return True
            if i>n:return False
            t = False
            if i+1<n:t = ((nums[i]==nums[i+1]) and func(i+2)) 
            if i+2<n:
                t |= ((nums[i]==nums[i+1]==nums[i+2]) and func(i+3))
                t |= (  (nums[i+1] == nums[i] + 1 and nums[i+2] == nums[i+1] + 1)  and func(i+3))
            return t
        return func(0)