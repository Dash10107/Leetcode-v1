class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        mod = 10**9+7
        @cache
        def func(i,j,l,d):
            if l==k:
                return d 
            if i==n and l<k:
                return 0
            t = func(i+1,i,l+1,min(d,nums[i]-nums[j]) if j!=-1 else mod)%mod
            s=func(i+1,j,l,d)%mod
            return (t+s)%mod
        return func(0,-1,0,mod)