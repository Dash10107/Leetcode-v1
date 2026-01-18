class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        heap = []
        for x,y,t in towers:
            if abs(x-center[0])+abs(y-center[1])<=radius:
                heappush(heap,(-t,x,y))
        if heap:return [heap[0][1],heap[0][2]]
        else:return [-1,-1]