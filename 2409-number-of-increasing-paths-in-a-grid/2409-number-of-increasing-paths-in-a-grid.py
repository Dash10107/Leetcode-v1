class Solution:
    def countPaths(self, mat: List[List[int]]) -> int:
        n,m = len(mat),len(mat[0])
        dp = {}
        mod = 10**9+7
        def dfs(r,c,prev):
            if r<0 or r==n or c<0 or c==m or mat[r][c]<=prev:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            res = 1
            res += dfs(r+1,c,mat[r][c])%mod
            res += dfs(r-1,c,mat[r][c])%mod
            res += dfs(r,c-1,mat[r][c])%mod
            res += dfs(r,c+1,mat[r][c])%mod
            dp[(r,c)]=res
            return res
        for i in range(n):
            for j in range(m):
                dfs(i,j,-1)
        return sum(dp.values())%mod