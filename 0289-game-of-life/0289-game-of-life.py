class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirr  = [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
        n = len(board);m=len(board[0])
        def count(i,j):
            c = 0
            for dr,dc in dirr:
                nr,nc = dr+i,dc+j
                if 0<=nr<n and 0<=nc<m:
                    c+=board[nr][nc]
            return c
        changes = set()
        for i in range(n):
            for j in range(m):
                c = count(i,j)
                curr = board[i][j]
                if curr==1 and c<2:
                    changes.add((i,j))
                elif  curr==1 and (c==2 or c==3):
                    continue
                elif curr==1 and c>3:
                    changes.add((i,j))
                elif curr==0 and c==3:
                    changes.add((i,j))
                else:
                    continue
        for i,j in changes:
            board[i][j] = 1-board[i][j]
        