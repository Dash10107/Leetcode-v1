class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        n,m =len(grid),len(grid[0])
        dist = [[float('inf')]*m for _ in range(n)]
        dirr = [(0,1),(1,0),(-1,0),(0,-1)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    q.append((i,j,0))
                    dist[i][j]=0
        while q:
            ii,jj,t = q.popleft()
            for dr,dc in dirr:
                nr,nc= ii+dr,jj+dc
                if 0<=nr<n and 0<=nc<m and grid[nr][nc]!=2 and t+1<dist[nr][nc]:
                    dist[nr][nc]= t+1
                    q.append((nr,nc,t+1))
        def func(tt):
            if dist[0][0] <= tt: return False
            qq =deque([(0,0,tt)])
            vis = [[False]*m for _ in range(n)]
            vis[0][0]=True
            while qq:
                ii,jj,t = qq.popleft()
                for dr,dc in dirr:
                    nr,nc= ii+dr,jj+dc
                    if 0<=nr<n and 0<=nc<m and not vis[nr][nc] and  grid[nr][nc]!=1 and grid[nr][nc]!=2:
                            if (nr,nc)==(n-1,m-1):
                                return t+1<=dist[nr][nc]
                            elif t+1<dist[nr][nc]:
                                qq.append((nr,nc,t+1))
                                vis[nr][nc]=True
            return False
        l = 0;r = 10**9
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if func(mid):
                ans = mid
                l= mid+1
            else:
                r = mid-1
        return ans