class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        mx = max(stones)
        @cache
        def func(i,t):
            if t>mx:return float('inf')
            if i==n:
                return abs(t)
            return min(func(i+1,stones[i]+t),func(i+1,t-stones[i]))
        return func(0,0)