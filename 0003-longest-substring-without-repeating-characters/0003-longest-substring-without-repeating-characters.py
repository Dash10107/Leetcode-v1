class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set();n=len(s)
        ans = 0;j=0
        for i in range(n):
            while s[i] in seen:
                seen.remove(s[j])
                j+=1
            seen.add(s[i])
            ans = max(ans,i-j+1)
        return ans