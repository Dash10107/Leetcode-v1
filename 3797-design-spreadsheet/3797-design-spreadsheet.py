class Spreadsheet:
    def __init__(self, rows: int):
        self.grid = [[0] * 26 for _ in range(rows)]  

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - ord("A")
        row = int(cell[1:]) - 1
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        col = ord(cell[0]) - ord("A")
        row = int(cell[1:]) - 1
        self.grid[row][col] = 0

    def getValue(self, formula: str) -> int:
        temp = 0
        formula = formula[1:] 
        parts = formula.split("+")
        for part in parts:
            if part[0].isdigit():  
                temp += int(part)
            else:  
                col = ord(part[0]) - ord("A")
                row = int(part[1:]) - 1
                temp += self.grid[row][col]
        return temp
