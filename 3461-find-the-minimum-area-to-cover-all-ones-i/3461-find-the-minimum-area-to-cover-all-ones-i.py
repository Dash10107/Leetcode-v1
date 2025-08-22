from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        min_row, min_col = float('inf'), float('inf')
        max_row, max_col = float('-inf'), float('-inf')

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    min_row = min(min_row, i)
                    min_col = min(min_col, j)
                    max_row = max(max_row, i)
                    max_col = max(max_col, j)

        height = max_row - min_row + 1
        width = max_col - min_col + 1
        return height * width
