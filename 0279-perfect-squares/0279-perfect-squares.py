class Solution:
    def numSquares(self, n: int) -> int:
        @cache
        def func(i):
            if i==0:
                return 0
            if i<0:
                return float('inf')
            curr = 1
            ans = i
            while curr**2<=i:
                ans = min(ans,1+func(i-curr**2))
                curr+=1
            return ans
        return func(n)
