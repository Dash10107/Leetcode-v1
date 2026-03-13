class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        pref=0
        c = {0:1};ans=0
        for a in arr:
            pref+=a
            if pref-k in c:
                ans+= c[pref-k]
            c[pref] = c.get(pref,0)+1
        return ans