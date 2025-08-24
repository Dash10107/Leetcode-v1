class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        mod = 10**9+7
        n = len(nums)
        @cache
        def func(i,cnt,s):
            if s==k:return 2**(n-cnt)
            if i==n or s>k:return 0
            take = func(i+1,cnt+1,s+nums[i])%mod
            nott  = func(i+1,cnt,s)%mod
            return (take+nott)%mod
        return func(0,0,0)