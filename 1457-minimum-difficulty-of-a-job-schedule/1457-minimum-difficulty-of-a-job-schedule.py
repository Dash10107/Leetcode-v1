class Solution:
    def minDifficulty(self, jobd: List[int], d: int) -> int:
        n = len(jobd)
        if d>n:return -1
        @cache
        def func(i,dd):
            if dd==1:
                return max(jobd[i:])
            ans = float('inf');m = 0
            for j in range(i,n-dd+1):
                m = max(jobd[j],m)
                ans = min(ans,m+func(j+1,dd-1))
            return ans
        ans = func(0,d)
        return ans if ans!=float('inf') else -1