class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        mask = 1<<n
        sums = [0]*mask
        for m in range(mask):
            s = 0
            for i in range(n):
                if m & (1<<i):
                    s+=cookies[i]
            sums[m]=s
        dp = [[float('inf')]*(k+1) for _ in range(mask)]
        dp[0][0]=0
        for m in range(1,mask):
            for g in range(1,k+1):
                sub  = m
                while sub:
                    rem = m^sub
                    dp[m][g] = min(dp[m][g],max(dp[rem][g-1],sums[sub]))
                    sub = (sub-1)&m
        return dp[mask-1][k]