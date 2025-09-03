from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        xs = sorted(set(x for x, y in points))
        ys = sorted(set(y for x, y in points))
        xm = {x: i+1 for i, x in enumerate(xs)}
        ym = {y: i+1 for i, y in enumerate(ys)}
        
        cmpp = [(xm[x], ym[y]) for x, y in points]
        n, m = len(xs), len(ys)
        
        grid = [[0]*(m+2) for _ in range(n+2)]
        for x, y in cmpp:
            grid[x][y] = 1
        
        ps = [[0]*(m+2) for _ in range(n+2)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                ps[i][j] = grid[i][j] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]
        
        def calc(x1, y1, x2, y2):
            if x1 > x2 or y1 > y2:
                return 0
            return ps[x2][y2] - ps[x1-1][y2] - ps[x2][y1-1] + ps[x1-1][y1-1]
        
        ans = 0
        for i in range(len(cmpp)):
            for j in range(len(cmpp)):
                if i == j:
                    continue
                xa, ya = cmpp[i]
                xb, yb = cmpp[j]
                if xa <= xb and ya >= yb: 
                    if calc(xa, yb, xb, ya) == 2:
                        ans += 1
        return ans
