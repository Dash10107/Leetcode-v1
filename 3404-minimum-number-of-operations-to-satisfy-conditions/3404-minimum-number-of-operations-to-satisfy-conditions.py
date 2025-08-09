class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        n= len(grid);m = len(grid[0])
        @lru_cache(None)
        def func(j,keep):
            if j>=m:return 0
            c = 0
            for i in range(n):
                c+= (1 if grid[i][j]!=keep else 0)
            ans = float('inf')
            for opt in range(0,10):
                if opt!=keep:
                    ans = min(ans,c+func(j+1,opt))
            return ans
        ans = float('inf')
        for j in range(0,10):
            ans = min(ans,func(0,j))
        return ans