class Solution:
    def findLHS(self, arr: List[int]) -> int:
        c = Counter(arr)
        ans = 0
        for ch in c:
            if ch-1 in c:
                ans = max(ans,c[ch]+c[ch-1])
            if ch+1 in c:
                ans = max(ans,c[ch]+c[ch+1])
        return ans