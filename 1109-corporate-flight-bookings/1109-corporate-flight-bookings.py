class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0]*n
        for f,l,s in bookings:
            f-=1;l-=1
            diff[f]+=s
            if l+1<n:diff[l+1]-=s
        ans = [0]*n
        curr=0
        for i in range(n):
            curr+=diff[i]
            ans[i]+=curr
        return ans