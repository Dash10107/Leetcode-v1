class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s = Counter(s)
        ans = ''
        for ch in order:
            if ch in s:
                ans+= ch*s[ch]
                s[ch]=0
        for ch in s:
            ans+= ch*s[ch]
        return ans
