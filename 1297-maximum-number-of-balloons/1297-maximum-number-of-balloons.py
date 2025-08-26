class Solution:
    def maxNumberOfBalloons(self, s: str) -> int:
        c =Counter(s)
        t= Counter("balloon")
        ans = float('inf')
        for ch in t:
            ans = min(ans,c[ch]//t[ch])
        return ans