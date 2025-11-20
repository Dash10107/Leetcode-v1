class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        ans = []
        intervals.sort(key=lambda x:(x[1],-x[0]))
        for s,e in intervals:
            c = (len(ans)>=1 and ans[-1]>=s)+(len(ans)>1 and ans[-2]>=s)
            if c<2:
                if c==0:ans.append(e-1)
                ans.append(e)
        return len(ans)