class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        n = len(grid);m=len(grid[0])
        @cache
        def func(i,j,c):
            if i>=n or j>=m:return float('-inf')
            cost = 1 if grid[i][j] else 0
            score = grid[i][j]
            if c+cost>k:return float('-inf')
            if i==n-1 and j==m-1:
                return score
            side = func(i+1,j,c+cost)
            down = func(i,j+1,c+cost)
            if max(side,down)==float('-inf'):return float('-inf')
            else:return score+max(side,down)
        ans =  func(0,0,0)
        return ans if ans!=float('-inf') else -1