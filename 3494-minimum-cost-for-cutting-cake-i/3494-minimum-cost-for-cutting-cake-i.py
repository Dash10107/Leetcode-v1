class Solution:
    def minimumCost(self, m: int, n: int, hcut: List[int], vcut: List[int]) -> int:
        hcut.sort(reverse=True)
        vcut.sort(reverse=True)
        i = j = 0
        hcnt = vcnt = 1
        ans = 0
        while i < len(hcut) and j < len(vcut):
            if hcut[i] >= vcut[j]:
                ans += hcut[i] * vcnt
                hcnt += 1
                i += 1
            else:
                ans += vcut[j] * hcnt
                vcnt += 1
                j += 1
        while i < len(hcut):
            ans += hcut[i] * vcnt
            i += 1
        while j < len(vcut):
            ans += vcut[j] * hcnt
            j += 1
        return ans
