class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def func(l,r,op):
            if r - l + 1 < 2:
                return 0
            c1,c2,c3 =0,0,0
            if l+1<=r and nums[l]+nums[l+1]==op:
                c1 =  func(l+2,r,op)+1
            if r-1>=l and nums[r]+nums[r-1]==op:
                c2 =  func(l,r-2,op)+1
            if nums[l]+nums[r]==op:
                c3 = func(l+1,r-1,op)+1
            return max(c1,c2,c3)
        if n>=2:
            return 1 + max(func(2,n-1,nums[0]+nums[1]),func(1,n-2,nums[0]+nums[-1]),func(0,n-3,nums[-1]+nums[-2]))
        else:
            return 1