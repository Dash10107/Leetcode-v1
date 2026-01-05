class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        neg_count = 0
        min_abs = float('inf')
        for row in matrix:
            for value in row:
                total+=abs(value)
                if value <0:
                    neg_count +=1
                min_abs = min(min_abs,abs(value))
        if neg_count % 2 == 1:
            total -=2*min_abs
        return total
        