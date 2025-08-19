class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = 1;i=1;n=len(s);curr=1
        while i<n:
            if ord(s[i])-1==ord(s[i-1]):
                curr+=1
                ans=max(ans,curr)
            else:
                curr=1
            i+=1
        return ans