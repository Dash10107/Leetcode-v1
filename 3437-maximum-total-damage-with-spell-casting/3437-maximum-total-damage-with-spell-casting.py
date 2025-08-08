class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        c = defaultdict(int)
        for i in power:c[i]+=1
        ans=0
        p = [0] + sorted(c.keys())
        nn = len(p)
        if nn-1==1:return c[p[1]]*p[1]
        dp = [0]*nn
        dp[1]= c[p[1]]*p[1]
        dp[2]= max(c[p[2]]*p[2] + (dp[1] if p[2]-p[1]>2 else 0),dp[1])
        for i in range(3,nn):
            dmg = p[i] * c[p[i]]
            if p[i]-p[i-1]>2:
                dp[i]= max(dp[i],dp[i-1]+dmg)
            if p[i]-p[i-2]>2:
                dp[i]= max(dp[i],dp[i-2]+dmg)
            dp[i]= max(dp[i],dp[i-1],dp[i-3]+dmg)
        return dp[nn-1]