class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        a,b = float('inf'),float('-inf')
        for ch in c.values():
            if ch&1:
                b = max(b,ch)
            else:
                a = min(a,ch)
        return b-a