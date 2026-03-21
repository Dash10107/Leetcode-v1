class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        l=x;r=x+k-1
        while l<r:
            for i in range(y,y+k):
                grid[l][i],grid[r][i]=grid[r][i],grid[l][i]
            l+=1
            r-=1
        return grid