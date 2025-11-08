class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        lines = defaultdict(int)
        for i,v in enumerate(ranges):
            start = max(0,i-v)
            end=min(n,i+v)
            lines[start]=max(lines[start],end)
        curr=lines[0];ans=1;nextt=0
        i=0
        while i<=n and curr<n:
            if i>curr:return -1
            elif i==curr:
                nextt= max(nextt,lines[i])
                ans+=1
                curr=nextt
                nextt=0
            else:
                nextt=max(nextt,lines[i])
            i+=1
        return ans
        