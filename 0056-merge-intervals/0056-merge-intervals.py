class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ans = []
        s,e = intervals[0][0],intervals[0][1]
        for inter in intervals[1:]:
            st,en = inter
            if st<=e:
                e = max(e,en)
            else:
                ans.append([s,e])
                s,e = st,en
        ans.append([s,e])
        return ans
