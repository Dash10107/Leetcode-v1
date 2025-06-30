class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[False] * n for _ in range(n)]    
        def issafe(board,r,c):
            for i in range(r):
                if board[i][c]:
                    return False
                # diaganlo lef
            for i in range(r+1):
                if c - i >= 0 and board[r - i][c - i]:  # Bounds check for left diagonal
                    return False

            for i in range(1, r + 1):
                if c + i < len(board) and board[r - i][c + i]:  # Bounds check for right diagonal
                    return False
            return True
        def func(b,r):
            if r==n:
                return 1
            count = 0
            for c in range(n):
                if issafe(b,r,c):
                    b[r][c]=True
                    count+=func(b,r+1)
                    b[r][c]=False
            return count
        return func(board,0)
