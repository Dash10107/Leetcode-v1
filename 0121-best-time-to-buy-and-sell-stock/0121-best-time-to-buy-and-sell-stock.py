class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        @lru_cache(None)
        def func(i,last,left):
            if i==n or left==0:return 0 
            ans = func(i+1,last,left)
            if last:
                ans = max(ans,prices[i]+func(i+1,0,left-1))
            else:
                ans = max(ans,-prices[i]+func(i+1,1,left))
            return ans
        return func(0,0,1)