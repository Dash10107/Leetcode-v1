class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m = len(heights),len(heights[0])
        pacific,atlantic = set(),set()
        def dfs(i,j,vis,prev):
            if (i,j) in vis:return
            if i<0 or i>=n or j<0 or j>=m:return
            if heights[i][j]<prev:return
            vis.add((i,j))
            for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr,nc = i+dr,j+dc
                dfs(nr,nc,vis,heights[i][j])
        for r in range(n):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,m-1,atlantic,heights[r][m-1])
        for c in range(m):
            dfs(0,c,pacific,heights[0][c])
            dfs(n-1,c,atlantic,heights[n-1][c])
        return list(pacific.intersection(atlantic))