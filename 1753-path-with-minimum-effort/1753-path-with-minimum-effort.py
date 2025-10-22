import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0,0,0)]
        n,m = len(heights),len(heights[0])
        dis = [[float(inf)]*m for _ in range(n)]
        dirr = [(0,1),(-1,0),(0,-1),(1,0)]
        dis[0][0]=0
        while heap:
            d,i,j=heappop(heap)
            if i==n-1 and j==m-1:return d
            for dr,dc in dirr:
                nr,nc=i+dr,j+dc
                if 0<=nr<n and 0<=nc<m:
                    new =  max(d,abs(heights[i][j]-heights[nr][nc]))
                    if new<dis[nr][nc]:
                       dis[nr][nc]=new
                       heappush(heap,(new,nr,nc))
        return 0