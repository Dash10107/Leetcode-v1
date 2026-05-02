class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers= [];n=len(wage)
        for i in range(n):
            rat = wage[i]/quality[i]
            workers.append((rat,quality[i]))
        workers.sort(key=lambda x:x[0])
        heap=[];curr=0;ans=float('inf')
        for ratio,q in workers:
            heappush(heap,-q)
            curr+=q
            if len(heap)>k:
                top = -heappop(heap)
                curr-=top
            if len(heap)==k:
                temp = curr*ratio
                ans=min(ans,temp)
        return ans