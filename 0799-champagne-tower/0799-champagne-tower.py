class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0]*(query_row+2)
        dp[0]=poured
        for r in range(query_row):
            for c in range(r,-1,-1):
                q = max(0.0,(dp[c]-1.0)/2.0)
                dp[c]=q
                dp[c+1]+=q
        return min(1.0,dp[query_glass])