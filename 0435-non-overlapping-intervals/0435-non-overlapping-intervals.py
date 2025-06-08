class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x:x[1])
        ans = 0
        end= intervals[0][1]
        for j in range(1,len(intervals)):
            if intervals[j][0]<end:
                ans+=1
            else:
                end = intervals[j][1]
        return ans

        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        