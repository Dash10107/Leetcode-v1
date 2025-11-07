class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        ans = [intervals[0]]
        c=0;end=0
        for s,e in intervals:
            if e>end:
                c+=1
                end=e
        return c