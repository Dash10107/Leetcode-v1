class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        base = 0
        for p,s in zip(prices,strategy):
            base+= (p*s)
        
        price = [0]*(n+1);prof=[0]*(n+1)
        for i in range(n):
            price[i+1]=  price[i]+prices[i]
            prof[i+1]= prof[i]+ (prices[i]*strategy[i])

        ans =base;half = k//2

        for i in range(n-k+1):
            old = prof[i+k]-prof[i]
            new = price[i+k]-price[i+half]
            ans = max(ans,base-old+new)
        return ans