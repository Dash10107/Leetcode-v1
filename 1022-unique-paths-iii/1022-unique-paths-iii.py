class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n = len(grid);m=len(grid[0]);c=m*n
        dirr = [(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:start = (i,j)
                elif grid[i][j]==2:end=(i,j)
                elif grid[i][j]==-1:c-=1
        self.ans=0
        def dfs(i,j,path):
            if path[-1]==end:
                if len(path)==c:self.ans+=1
                return
            for dr,dc in dirr:
                nr,nc = i+dr,j+dc
                if 0<=nr<n and 0<=nc<m and grid[i][j]!=-1 and (nr,nc) not in path:
                    dfs(nr,nc,path+[(nr,nc)])
        dfs(start[0],start[1],[start])
        return self.ans