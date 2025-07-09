class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        ct = 0;ans=0;l=0
        for r in range(n):
            ct+= abs(ord(s[r])-ord(t[r]))
            while ct>maxCost:
                ct-= abs(ord(s[l])-ord(t[l]))
                l+=1
            ans = max(ans,r-l+1)
        return ans