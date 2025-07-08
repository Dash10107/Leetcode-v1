class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def func(i,buy):
            if i>=len(prices):
                return 0
            if buy==-1:
                return func(i+1,prices[i])
            hold = func(i+1,buy)
            sell = prices[i]-buy  + func(i+2,-1)
            start = func(i+1,prices[i])
            return max(hold,sell,start)
        return func(0,-1)