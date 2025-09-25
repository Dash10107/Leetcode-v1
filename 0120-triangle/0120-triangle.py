class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        @cache
        def func(i,j):
            if i==n-1:
                return triangle[i][j]
            down  = triangle[i][j]+func(i+1,j)
            diag = triangle[i][j]+func(i+1,j+1)
            return min(down,diag)
        return func(0,0)