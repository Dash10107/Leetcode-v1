class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        mr=[]
        n=len(grid);m=len(grid[0])
        for row in grid:
            j=m-1;ct=0
            while j>=0 and row[j]==0:
                j-=1;ct+=1
            mr.append(ct)
        ans=0

        for i in range(n):
            need = m-i-1
            j=i
            while j<n and mr[j]<need:
                j+=1
            if j==n:return -1
            
            while j>i:
                mr[j],mr[j-1]=mr[j-1],mr[j]
                j-=1
                ans+=1
        return ans
        
