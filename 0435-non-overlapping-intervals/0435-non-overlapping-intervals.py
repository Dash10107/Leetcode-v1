class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        curr,ans=intervals[0][1],0
        for s,e in intervals[1:]:
            if s<curr:ans+=1
            else:curr=e
        return ans