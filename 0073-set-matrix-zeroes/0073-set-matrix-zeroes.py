class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        cols = []
        rows = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    cols.append(j)
                    rows.append(i)
        
        for j in cols:
            for k in range(n):
                matrix[k][j]=0
        for i in rows:
            matrix[i]=[0]*m
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        