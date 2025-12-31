class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dirr = [(0,1),(1,0),(-1,0),(0,-1)]        
        def can(mid):
            grid =  [[0]*col for _ in range(row)]
            for i in range(mid):
                grid[cells[i][0]-1][cells[i][1]-1]=1
            vis = set()
            def dfs(i,j):
                if (i,j) in vis:return False
                if i==row-1:return True
                vis.add((i,j))
                for dr,dc in dirr:
                    nr,nc = dr+i,dc+j
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]==0:
                        if dfs(nr,nc):return True
                return False
            for i in range(col):
                if grid[0][i]==0:
                    if dfs(0,i):
                        return True
            return False
        
        ans = 1
        left = 1;right=len(cells)-1
        while left<=right:
            mid = (left+right)//2
            if can(mid):
                ans = mid
                left = mid+1
            else:
                right=mid-1
        return ans