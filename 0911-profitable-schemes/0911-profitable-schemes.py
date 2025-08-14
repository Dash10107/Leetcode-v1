class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10**9+7
        m = len(group)
        @cache
        def func(i,p,nn):
            if i==m:
                return 1 if   p>=minProfit else 0
            nottake = func(i+1,p,nn)%mod
            take = 0
            if group[i]<=nn:
                newp = min(minProfit,p+profit[i])
                take += func(i+1,newp,nn-group[i])%mod
            return (take+nottake)%mod
        return func(0,0,n)%mod