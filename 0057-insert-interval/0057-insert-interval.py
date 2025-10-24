class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        ans = []
        i,n = 0,len(intervals)
        s,e=new
        while i<n and intervals[i][1]<s:
            ans.append(intervals[i])
            i+=1
        while i<n and intervals[i][0]<=e:
            s = min(s,intervals[i][0])
            e= max(e,intervals[i][1])
            i+=1
        ans.append([s,e])
        while i<n:
            ans.append(intervals[i])
            i+=1
        return ans