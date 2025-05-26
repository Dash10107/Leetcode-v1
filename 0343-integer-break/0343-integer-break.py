class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3:
            return n-1
        @cache
        def f(i):
            if i in [1,2,3]:
                return i
            if i<2:
                return float('-inf')
            ans = 0
            for j in range(2,i+1):
                ans = max(ans,j*f(i-j))
            return ans
        return f(n)
  