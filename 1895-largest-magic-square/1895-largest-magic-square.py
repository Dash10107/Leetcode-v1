class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        
        n,m = len(grid),len(grid[0])
        
        row = [[0]*(m+1) for _ in range(n)]
        col = [[0]*m for _ in range(n+1)]
        d1 = [[0]*(m+1) for _ in range(n+1)]
        d2 = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                row[i][j+1]= row[i][j]+grid[i][j]
                col[i+1][j]=col[i][j]+grid[i][j]
                d1[i+1][j+1]=d1[i][j]+grid[i][j]
                d2[i+1][j]=d2[i][j+1]+grid[i][j]
        def check(i,j,k):
            s = row[i][j+k]-row[i][j]
            if d1[i+k][j+k]-d1[i][j] !=s:return False
            if d2[i+k][j]-d2[i][j+k]!=s:return False
            for t in range(k):
                if (row[i+t][j+k]-row[i+t][j] !=s) or (col[i+k][j+t]-col[i][j+t]!=s):
                    return False
            return True

        for k in range(min(n,m),1,-1):
            for i in range(n-k+1):
                for j in range(m-k+1):
                        if check(i,j,k):
                            return k
        return 1