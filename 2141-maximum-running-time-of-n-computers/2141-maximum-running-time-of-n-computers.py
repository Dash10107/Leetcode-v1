class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        s = sum(batteries)
        l,r = 0,s//n
        while l<r:
            mid = (l+r+1)//2
            ext = 0
            for p in batteries:ext+=min(p,mid)
            if ext>=n*mid:
                l=mid
            else:r=mid-1
        return l