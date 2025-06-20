class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n = len(board)
        m = len(board[0])
        dirr = [(0,1),(1,0),(-1,0),(0,-1)]
        vis = [[False]*m for _ in range(n)]
        def dfs(i,j):
            if vis[i][j]:
                return
            vis[i][j]=True
            for dr,dc in dirr:
                nr,nc = i+dr,j+dc
                if 0<=nr<n and 0<=nc<m and board[nr][nc]=='X' and (not vis[nr][nc]):
                    dfs(nr,nc)
        ans = 0
        for i in range(n):
            for j in range(m):
                if board[i][j]=='X' and not vis[i][j]:
                    dfs(i,j)
                    ans+=1
        return ans