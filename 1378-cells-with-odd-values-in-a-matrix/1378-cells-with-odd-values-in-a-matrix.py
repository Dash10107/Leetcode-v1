class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat = [[0]*n for _ in range(m)]
        for r,c in indices:
            for j in range(n):
                mat[r][j]+=1
            for i in range(m):
                mat[i][c]+=1
        c = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]&1:
                    c+=1
        return c