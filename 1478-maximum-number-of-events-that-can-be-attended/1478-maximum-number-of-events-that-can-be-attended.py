class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        ans = 0
        i,n = 0,len(events)
        last = max(e for _,e in events)
        for day in range(1,last+1):
            while i<n and events[i][0]==day:
                heappush(heap,events[i][1])
                i+=1
            while heap and heap[0]<day:
                heappop(heap)
            if heap:
                heappop(heap)
                ans+=1
            if i==n and not heap:break
        return ans