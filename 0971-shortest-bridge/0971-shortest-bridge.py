class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        vis= [[False]*n for _ in range(n)]
        q = deque([])
        dirr = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(i,j,q,vis):
            if 0>i or i>=n or 0>j or j>=n  or vis[i][j] or grid[i][j]==0:
                return
            vis[i][j]=True
            q.append((i,j,0))
            for dr,dc in dirr:
                dfs(i+dr,j+dc,q,vis)
        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    dfs(i,j,q,vis)
                    found = True
                    break
            if found:break
        while q:
            i,j,lev = q.popleft()
            for dr,dc in dirr:
                if 0<=i+dr<n and 0<=j+dc<n and (not vis[i+dr][j+dc]):
                    if grid[i+dr][j+dc]==1:
                        return lev
                    q.append((i+dr,j+dc,lev+1))
                    vis[i+dr][j+dc]=True
        return -1