class Solution:
    def onesMinusZeros(self, mat:List[List[int]]) -> List[List[int]]:
        n,m = len(mat),len(mat[0])
        prefRow = [0]*n;prefCol=[0]*m
        zeroRow = [0]*n;zeroCol=[0]*m
        for i in range(n):
            for j in range(m):
                prefRow[i]+=mat[i][j]
                prefCol[j]+=mat[i][j]
                zeroRow[i]+= 1 if mat[i][j]==0 else 0
                zeroCol[j]+= 1 if mat[i][j]==0 else 0
        diff = [[0]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                diff[i][j]=prefRow[i]+prefCol[j]-zeroRow[i]-zeroCol[j]
        return diff