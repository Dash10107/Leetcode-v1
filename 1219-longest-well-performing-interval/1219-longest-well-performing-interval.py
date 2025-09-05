class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        pref = [0]
        for i in range(n):
            pref.append( pref[i]+(1 if hours[i]>8 else -1))
        arr = []
        for i,v in enumerate(pref):
            if not arr or v<pref[arr[-1]]:
                arr.append(i)
        ans = 0
        for j in range(n,-1,-1):
            while arr and pref[j]>pref[arr[-1]]:
                ans = max(ans,j-arr.pop())
        return ans