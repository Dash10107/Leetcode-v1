class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        n = 3;m=3
        for i in range(n-1):
            for j in range(m-1):
                b = grid[i][j];c=1;t=4
                if  grid[i+1][j]==b:c+=1
                else:t-=1
                if  grid[i][j+1]==b:c+=1
                else:t-=1
                if  grid[i+1][j+1]==b:c+=1
                else:t-=1
                if c>=3 or t<=1:return True
        return False
