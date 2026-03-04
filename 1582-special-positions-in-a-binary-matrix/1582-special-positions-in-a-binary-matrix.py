class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n,m = len(mat),len(mat[0])
        prefRow = [0]*n;prefCol=[0]*m
        for i in range(n):
            for j in range(m):
                prefRow[i]+=mat[i][j]
                prefCol[j]+=mat[i][j]
        ans =0
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1 and prefRow[i]==1 and prefCol[j]==1:
                    ans+=1
        return ans