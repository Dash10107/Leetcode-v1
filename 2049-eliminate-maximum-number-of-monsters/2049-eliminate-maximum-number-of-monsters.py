class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        times = []
        for d,s in zip(dist,speed):
            time = (d+(s-1))//s
            heappush(times,time)
        i=0
        while i<n:
            time = heappop(times)
            if i>=time:return i
            i+=1
        return n