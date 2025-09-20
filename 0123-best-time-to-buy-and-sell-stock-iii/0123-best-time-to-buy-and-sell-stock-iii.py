class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        @cache
        def func(i,buy,lim):
            if i==n or lim==0:
                 return 0
            ans = func(i+1,buy,lim)
            if buy:
                ans = max(ans,prices[i]+func(i+1,False,lim-1))
            else:
                ans = max(ans,func(i+1,True,lim) - prices[i])
            return ans
        return func(0,False,2)