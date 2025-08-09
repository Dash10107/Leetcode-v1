class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dirr = [(-2,-1),(-1,-2),(1,-2),(-1,2),(2,1),(1,2),(-2,1),(2,-1)]
        @lru_cache(None)
        def func(r,c,kk):
            if 0>r or r>=n or c<0 or c>=n:
                return 0
            if kk==0:
                return 1
            p = 0
            for i in range(0,8):
                p+= func(r+dirr[i][0],c+dirr[i][1],kk-1)/8
            return p
        return func(row,column,k)