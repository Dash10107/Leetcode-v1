class Solution:
    def maxProfit(self, kk: int, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        @cache
        def func(i,buy,k):
            if i==n or k==0:
                 return 0
            ans = func(i+1,buy,k)
            if buy:
                ans = max(ans,prices[i]+func(i+1,False,k-1))
            else:
                ans = max(ans,func(i+1,True,k) - prices[i])
            return ans
        return func(0,False,kk)