class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dpp = [[[-1]*3 for _ in range(k+1)] for _ in range(n+1)]
        def dp(i,done,typee):
            if i==n:
                return 0 if typee==0 else float('-inf')
            if dpp[i][done][typee]!= -1:
                return dpp[i][done][typee]
            ans = 0
            if typee==0:
                ans = dp(i+1,done,0)
                if done<k:
                    ans = max(ans,-prices[i]+dp(i+1,done,1),prices[i]+dp(i+1,done,2))
            elif typee==1:
                ans = max( prices[i]+dp(i+1,done+1,0),dp(i+1,done,1))
            else:
                ans = max(-prices[i]+dp(i+1,done+1,0),dp(i+1,done,2))
            dpp[i][done][typee]=ans
            return ans
        return dp(0,0,0)