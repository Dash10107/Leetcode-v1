class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans= []
        for i in range(len(board)):
            for j in range(len(board)):
                ele = board[i][j]
                if ele != '.':
                    ans+=[(i,ele),(ele,j),(ele,i//3,j//3)]
        return len(ans)==len(set(ans))