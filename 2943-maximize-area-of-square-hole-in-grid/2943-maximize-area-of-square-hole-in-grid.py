class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        hl = len(hBars)
        hx,hy = 1,1
        for i in range(1,hl):
            if hBars[i]==hBars[i-1]+1:
                hx+=1
            else:
                hx=1
            hy = max(hy,hx)
        vx,vy = 1,1
        vl = len(vBars)
        for i in range(1,vl):
            if vBars[i]==vBars[i-1]+1:
                vx+=1
            else:
                vx=1
            vy = max(vy,vx)
        area = min(vy,hy)+1
        return area*area
