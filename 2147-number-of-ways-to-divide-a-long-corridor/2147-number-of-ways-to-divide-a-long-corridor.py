class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9+7
        dp = [[-1]*3 for _ in range(len(corridor))]
        def count(ind,seats):
            if ind==len(corridor):
                return 1 if seats==2 else 0
            if dp[ind][seats]!=-1:
                return dp[ind][seats]
            if seats==2:
                if corridor[ind]=='S':
                    res = count(ind+1,1)
                else:
                    res = (count(ind+1,0)+count(ind+1,2))%mod
            else:
                if corridor[ind]=='S':
                    res = count(ind+1,seats+1)
                else:
                    res = count(ind+1,seats)
            dp[ind][seats] =res
            return res
        return count(0,0)