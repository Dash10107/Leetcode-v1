class Solution:
    def maxProfit(self, p: List[int]) -> int:
        m = p[0];ans=0;n=len(p)
        for i in range(n):
            c = p[i]-m
            ans = max(ans,c)
            m = min(m,p[i])
        return ans