class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        @cache
        def func(i):
            if i==n:return 0
            if i>n:return float('inf')
            ans = float('inf')
            for jump in (1,2,3):
                j = i+jump
                if j<=n:
                    cost = costs[j-1]+(jump*jump)+ func(j)
                    ans = min(cost,ans)
            return ans
        return func(0)