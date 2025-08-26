class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        c =Counter(s)
        t= Counter(target)
        ans = float('inf')
        for ch in t:
            ans = min(ans,c[ch]//t[ch])
        return ans