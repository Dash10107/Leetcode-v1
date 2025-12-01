class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        r = max(time)*totalTrips
        l = 1
        while l<=r:
            mid = (l+r+1)//2
            c = 0
            for t in time:
                c += mid//t
            if c>=totalTrips:
                r = mid-1
            else:
                l = mid+1
        return l