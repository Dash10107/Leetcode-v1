class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m = len(pizza);n = len(pizza[0])
        pref = [[0]*(n+1) for _ in range(m+1)]
        mod = 10**9+7
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                pref[r][c]= pref[r+1][c]+pref[r][c+1]-pref[r+1][c+1] + (1 if pizza[r][c]=='A' else 0)
        @cache
        def func(i,j,c):
            if pref[i][j]==0:return 0
            if c==0:return 1
            ans = 0
            for nr in range(i+1,m):
                if pref[i][j]-pref[nr][j]>0:
                    ans = (ans + func(nr,j,c-1))%mod
            for nc in range(j+1,n):
                if pref[i][j]-pref[i][nc]>0:
                    ans = (ans+ func(i,nc,c-1))%mod
            return ans%mod
        return func(0,0,k-1)