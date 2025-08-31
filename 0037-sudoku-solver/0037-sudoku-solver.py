class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [[set() for _ in range(3)] for _ in range(3)]
        empty_cells = []  
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty_cells.append((i, j))
                else:
                    n = board[i][j]
                    rows[i].add(n)
                    cols[j].add(n)
                    grids[i//3][j//3].add(n)

        empty_cells = [
            (9 - len(rows[i] | cols[j] | grids[i//3][j//3]), i, j)
            for i, j in empty_cells
        ]
        heapify(empty_cells)  
        def isv(i, j, n):
            return n not in rows[i] and n not in cols[j] and n not in grids[i//3][j//3]

        def func():
            if not empty_cells:
                return True

            _, i, j = heappop(empty_cells)
            for n in '123456789':
                if isv(i, j, n):
                    board[i][j] = n
                    rows[i].add(n)
                    cols[j].add(n)
                    grids[i//3][j//3].add(n)

                    if func():
                        return True

                    board[i][j] = '.'
                    rows[i].remove(n)
                    cols[j].remove(n)
                    grids[i//3][j//3].remove(n)


            heappush(empty_cells, (9 - len(rows[i] | cols[j] | grids[i//3][j//3]), i, j))
            return False

        func()
