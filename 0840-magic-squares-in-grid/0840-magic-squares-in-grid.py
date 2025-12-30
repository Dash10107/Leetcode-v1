class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        def isMagic(row,col):
            seen = [False]*10
            rows = [0]*3;cols=[0]*3
            for ii in range(3):
                for jj in range(3):
                    num = grid[row+ii][col+jj]
                    if 1>num or 9<num:return False
                    rows[ii]+=num
                    cols[jj]+=num
                    if seen[num]:return False
                    seen[num]=True
            diag1 = grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]
            diag2 = grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]
            if diag1==diag2==rows[0]==rows[1]==rows[2]==cols[0]==cols[1]==cols[2]:return True
            else:return False


        n = len(grid);m=len(grid[0])
        for i in range(n-2):
            for j in range(m-2):
                if isMagic(i,j):
                    ans+=1
        return ans
