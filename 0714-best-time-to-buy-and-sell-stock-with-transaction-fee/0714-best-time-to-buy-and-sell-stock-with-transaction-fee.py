class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        ans = 0
        @cache
        def func(i,buy):
            if i==n:
                 return 0
            ans = func(i+1,buy)
            if buy:
                ans = max(ans,prices[i]+func(i+1,False))
            else:
                ans = max(ans,func(i+1,True) - prices[i]-fee)
            return ans
        return func(0,False)