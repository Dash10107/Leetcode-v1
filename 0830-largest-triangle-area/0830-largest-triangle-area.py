class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points);ans=0
        for i in range(n):
            for j in range(i,n):
                for k in range(j,n):
                    x1,y1 = points[i]
                    x2,y2 = points[j]
                    x3,y3 = points[k]
                    area =  abs(0.5*(x1*(y2-y3)+ x2*(y3-y1)+x3*(y1-y2) ))
                    ans = max(ans,area)
        return ans