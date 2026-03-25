class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid);m=len(grid[0])
        row = [0]*n;col=[0]*m
        for i in range(n):
            for j in range(m):
                row[i]+=grid[i][j]
                col[j]+=grid[i][j]
        suffr=[0]*(n+1);suffc=[0]*(m+1)
        for i in range(n-1,-1,-1):
            suffr[i]= suffr[i+1]+row[i]
        for j in range(m-1,-1,-1):
            suffc[j]=suffc[j+1]+col[j]
        ans = 0
        prefr = 0;prefc=0
        for i in range(n):
            if prefr==suffr[i]:
                return True
            prefr+=row[i]
        for j in range(m):
            if prefc==suffc[j]:
                return True
            prefc+=col[j]
        return False