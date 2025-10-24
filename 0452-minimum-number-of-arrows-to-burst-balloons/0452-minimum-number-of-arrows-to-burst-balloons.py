class Solution:
    def findMinArrowShots(self, intervals: List[List[int]]) -> int:
        if not intervals:return 0
        intervals.sort(key=lambda x:x[1])
        ans=1;end=intervals[0][1]
        for s,e in intervals[1:]:
            if s>end:
                ans+=1
                end=e
        return ans