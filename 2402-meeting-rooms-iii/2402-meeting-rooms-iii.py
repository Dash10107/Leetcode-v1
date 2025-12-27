class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free = list(range(n))
        heapify(free)
        busy = []
        count = [0]*n
        for s,e in meetings:
            dur = e-s
            while busy and busy[0][0]<=s:
                _,room = heappop(busy)
                heappush(free,room)
            if free:
                room = heappop(free)
                count[room]+=1
                heappush(busy,(e,room))
            else:
                time,room = heappop(busy)
                count[room]+=1
                heappush(busy,(time+dur,room))
            
        ans = max(count)
        for i,c in enumerate(count):
            if c == ans:
                return i