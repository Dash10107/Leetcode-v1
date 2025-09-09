class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        n = len(grid);m=len(grid[0])
        for i in range(n):
            for j in range(m):
                top=left=True
                if i+1<n:top= (grid[i][j]==grid[i+1][j])
                if j+1<m:left = (grid[i][j]!=grid[i][j+1])
                if not top or not left:
                    return False
        return True