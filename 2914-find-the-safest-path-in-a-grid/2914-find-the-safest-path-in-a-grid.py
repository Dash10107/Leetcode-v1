class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = m = len(grid)
        dist = [[0]*n for _ in range(m)]
        vis = [[False]*n for _ in range(m)]
        dirr = [(0,1),(1,0),(-1,0),(0,-1)]
        q = deque([])
        l,r = 0,0
        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    q.append((i,j,0))
                    vis[i][j]=True
        while q:
            i,j,lev = q.popleft()
            vis[i][j]=True
            dist[i][j]=lev
            r = max(r,lev)
            for dr,dc in dirr:
                nr,nc = i+dr,j+dc
                if 0<=nr<n and 0<=nc<m and not vis[nr][nc]:
                    vis[nr][nc]=True
                    q.append((nr,nc,lev+1))
        def bfs(mid):
            q = deque([])
            vis = [[False]*n for _ in range(n)]
            if dist[0][0]<mid:return False
            q.append((0,0))
            vis[0][0]=True
            while q:
                i,j = q.popleft()
                if i==n-1 and j==m-1:return True
                for dr,dc in dirr:
                    nr,nc = i+dr,j+dc
                    if 0<=nr<n and 0<=nc<n and not vis[nr][nc] and dist[nr][nc]>=mid:
                        vis[nr][nc]=True
                        q.append((nr,nc))
            return False
        while l<=r:
            mid = (l+r)//2
            if bfs(mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1
        return ans