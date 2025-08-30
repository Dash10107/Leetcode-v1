class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0;n=len(s)
        for i in range(n-2):
            if len(set(s[i:i+3]))==3:
                ans+=1
        return ans