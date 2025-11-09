class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        non = 0;i=0;n=len(ranges)
        while i<n:
            s,e = ranges[i]
            j=i+1
            while j<n and e>=ranges[j][0]:
                e = max(e,ranges[j][1])
                j+=1
            non+=1
            i=j
        return pow(2, non, 10**9+7)