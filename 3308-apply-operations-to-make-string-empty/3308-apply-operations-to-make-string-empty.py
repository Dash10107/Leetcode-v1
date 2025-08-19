class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        c = Counter(s)
        m = max(c.values())
        ans = ''
        last = set()
        for ch in reversed(s):
            if c[ch]==m and ch not in last:
                ans+=ch
                last.add(ch)
        return ans[::-1]