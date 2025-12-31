class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dirr = [(0,1),(1,0),(-1,0),(0,-1)]        
        def can(mid):
            grid =  [[0]*col for _ in range(row)]
            for i in range(mid):
                grid[cells[i][0]-1][cells[i][1]-1]=1
            vis = set()
            q = deque([])
            for i in range(col):
                if grid[0][i]==0:
                    q.append((0,i))
                    vis.add((0,i))
            while q:
                i,j = q.popleft()
                if i==row-1:return True
                for dr,dc in dirr:
                    nr,nc = dr+i,dc+j
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]==0 and (nr,nc) not in vis:
                        q.append((nr,nc))
                        vis.add((nr,nc))
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