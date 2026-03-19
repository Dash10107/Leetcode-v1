class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n,m = len(grid),len(grid[0])
        ans = 0
        px = [[0]*m for i in range(n)]
        py = [[0]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                px[i][j]= 1 if grid[i][j]=='X' else 0
                py[i][j]=1 if grid[i][j]=='Y' else 0
                if i-1>=0:
                    px[i][j]+= px[i-1][j]
                    py[i][j]+= py[i-1][j]
                if j-1>=0:
                    px[i][j]+=px[i][j-1]
                    py[i][j]+=py[i][j-1]
                if i-1>=0 and j-1>=0:
                    px[i][j]-=px[i-1][j-1]
                    py[i][j]-=py[i-1][j-1]
                if px[i][j]==py[i][j] and px[i][j]>0:
                    ans+=1
        return ans