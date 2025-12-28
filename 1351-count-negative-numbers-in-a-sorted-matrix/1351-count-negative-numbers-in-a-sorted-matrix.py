class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid);m=len(grid[0])
        for row in grid:
            idx = m-bisect_left(row[::-1],0)
            if 0<=idx<m:ans+= m-idx
        return ans