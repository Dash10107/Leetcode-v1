class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        @cache
        def func(i,rem):
            if i==n:
                return 0
            m = 1
            for j in range(i-1,-1,-1):
                if nums[i]==nums[j]:
                    m = max(m,1+func(j,rem))
                elif nums[i]!=nums[j] and rem>0:
                    m = max(m,1+func(j,rem-1))
            return m
        ans = 0
        for i in range(n):
            ans = max(ans,func(i,k))
        return ans