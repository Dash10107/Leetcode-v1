class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        n = len(grid);m =len(grid[0])
        @cache
        def func(i,j,k):
            if (0>k or k>=m) or (0>j or j>=m):return 0
            if i==n:return 0
            res = 0
            res+= grid[i][j]
            if j!=k:res+= grid[i][k]
            new = 0
            for x in range(j-1,j+2):
                for y in range(k-1,k+2):
                    new = max(new,func(i+1,x,y))
            res+= new
            return res
        return func(0,0,m-1)