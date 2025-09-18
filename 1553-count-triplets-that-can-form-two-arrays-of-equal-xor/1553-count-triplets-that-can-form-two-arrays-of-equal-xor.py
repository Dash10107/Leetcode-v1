class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0;n=len(arr)
        pref = [0]*(n+1)
        for i in range(n):pref[i+1]=pref[i]^arr[i]
        for i in range(n):
            for k in range(i+1,n+1):
                if pref[k]==pref[i]:
                    ans+= k-(i+1)
        return ans