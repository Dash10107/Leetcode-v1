class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort()
        starts = [s for s,_,_ in events]
        @cache
        def func(i,kk):
            if kk==0 or i==n:
                return 0
            ii = bisect_left(starts,events[i][1]+1)
            attend = events[i][2] + func(ii,kk-1)
            skip = func(i+1,kk)
            return max(attend,skip)
        return func(0,k)