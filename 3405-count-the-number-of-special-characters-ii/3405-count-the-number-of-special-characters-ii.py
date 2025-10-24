from collections import defaultdict

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c = defaultdict(int)
        for i, ch in enumerate(word):
            if ch.islower():
                c[ch]=i
            elif ch not in c:
                c[ch]=i
        ans = 0
        for ch in range(ord('a'), ord('z') + 1):
            lower = chr(ch)
            upper = lower.upper()
            if lower in c and upper in c and c[lower] < c[upper]:
                ans += 1
        return ans
