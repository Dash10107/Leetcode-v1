class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = 0
        def check(st):
            for ch in st:
                if ch.upper() in st and ch.lower() in st:
                    continue
                else:
                    return False
            return True
        ans = ''
        for i in range(len(s)):
            for j in range(len(s)):
                if check(s[i:i+j+1]):
                    if len(ans)<len(s[i:i+j+1]):
                        ans = s[i:i+j+1]
        return ans