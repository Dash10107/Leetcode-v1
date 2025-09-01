class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap = [];n = len(apples)
        ans=0;i=0
        while i<n or heap:
            if i<n and apples[i]>0:
                heappush(heap,(i+days[i],apples[i]))
            while heap and heap[0][0]<=i:
                heappop(heap)
            if heap:
                exp,cnt = heappop(heap)
                cnt-=1
                ans+=1
                if cnt>0:
                    heappush(heap,(exp,cnt))
            i+=1
        return ans