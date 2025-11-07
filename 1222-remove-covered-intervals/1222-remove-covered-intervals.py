class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        ans = [intervals[0]]
        k=0
        for s,e in intervals[1:]:
            if s>=ans[-1][0] and e<=ans[-1][1]:
                k+=1
            elif s>ans[-1][1]:
                ans.append([s,e])
            elif s>ans[-1][0] and s<=ans[-1][1]:
                ans[-1][1]=max(ans[-1][1],e)
        return len(intervals)-k