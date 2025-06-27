class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9+7
        dirr = [(0,1),(1,0),(-1,0),(0,-1)]
        @cache
        def func(i,j,mm):
            if 0>i or i>=m or 0>j or j>=n:
                return 1
            if mm<=0 :
                return 0
            c = 0 
            for dr,dc in dirr:
                c+=func(i+dr,j+dc,mm-1)%mod
            return c%mod
        return func(startRow,startColumn,maxMove)
        
            