class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points);ans=0
        for i in range(n):
            for j in range(n):
                if i==j:continue
                if points[i][0]<=points[j][0] and points[i][1]>=points[j][1]:
                    val = True
                    for k in range(n):
                        if k==i or k==j:continue
                        xk,yk= points[k]
                        if points[i][0]<=xk<=points[j][0] and points[j][1]<=yk<=points[i][1]:
                            val = False
                            break
                    if val:
                        ans+=1
        return ans