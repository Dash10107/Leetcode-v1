class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n,m = len(grid),len(grid[0])
        mod = 12345
        ans = [[0]*m for _ in range(n)]
        pref = 1
        for i in range(n):
            for j in range(m):
                ans[i][j]=pref
                pref=(pref*grid[i][j])%mod
        suff=1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                ans[i][j]= (ans[i][j]*suff)%mod
                suff=(suff*grid[i][j])%mod
        return ans