class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        ans = 0
        mod = 10**9+7
        n,m = len(grid),len(grid[0])
        maxt = [[0]*m for i in range(n)]
        mint = [[0]*m for i in range(n)]
        maxt[0][0]=mint[0][0]=grid[0][0]
        for i in range(1,m):
            maxt[0][i]=mint[0][i] = maxt[0][i-1]*grid[0][i]
        for i in range(1,n):
            maxt[i][0]=mint[i][0]=maxt[i-1][0]*grid[i][0]
        for i in range(1,n):
            for j in range(1,m):
                if grid[i][j]>=0:
                    maxt[i][j]=(
                        max(maxt[i][j-1],maxt[i-1][j])*grid[i][j]
                    )
                    mint[i][j]=(
                        min(mint[i][j-1],mint[i-1][j])*grid[i][j]
                    )
                else:
                    maxt[i][j]=(
                        min(mint[i][j-1],mint[i-1][j])*grid[i][j]
                    )
                    mint[i][j]=(
                        max(maxt[i][j-1],maxt[i-1][j])*grid[i][j]
                    )
        if maxt[n-1][m-1]<0:return -1
        else:return maxt[n-1][m-1]%mod