class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points);ans=0
        grid = [[0]*52 for _ in range(52)]
        for x,y in points:
            grid[x+1][y+1]=1
        ps = [[0]*52 for _ in range(52)]
        for i in range(1,52):
            for j in range(1,52):
                ps[i][j] = grid[i][j]+ ps[i-1][j]+ ps[i][j-1] - ps[i-1][j-1]
        def calc(x1,y1,x2,y2):
            return ps[x2][y2] - ps[x1-1][y2]-ps[x2][y1-1] + ps[x1-1][y1-1]
        ans = 0
        for i in range(n):
            for j in range(n):
                x1,y1 = points[i];x2,y2 = points[j]
                if x1<=x2 and y1>=y2:
                    ans+= (1 if calc(x1+1,y2+1,x2+1,y1+1)==2 else 0)
        return ans