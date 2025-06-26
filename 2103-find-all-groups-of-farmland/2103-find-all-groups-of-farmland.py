class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n,m = len(land),len(land[0])
        vis= [[False]*m for _ in range(n)]
        dirr = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(i,j):
            nonlocal li
            nonlocal lj
            vis[i][j]=True
            if i>=li and j>=lj:
                li,lj=i,j
            for dr,dc in dirr:
                nr,nc = i+dr,j+dc
                if 0<=nr<n and 0<=nc<m and not vis[nr][nc] and land[nr][nc]==1:
                    dfs(nr,nc)
        ans = []
        for i in range(n):
            for j in range(m):
                if land[i][j]==1 and not vis[i][j]:
                    li,lj = i,j
                    dfs(i,j)
                    ans.append([i,j,li,lj])
        return ans