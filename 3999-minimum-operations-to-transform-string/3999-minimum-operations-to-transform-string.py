class Solution:
    def minOperations(self, s: str) -> int:
        ans = 0
        for ch in s:
            ans = max(ans,(26-(ord(ch)-ord('a')))%26)
        return ans