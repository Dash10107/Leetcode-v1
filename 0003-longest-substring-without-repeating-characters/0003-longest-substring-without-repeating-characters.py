class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        l,r,ans=0,0,0
        while r<len(s):
            if s[r] in dic and dic[s[r]]>=l:
                    l=dic[s[r]]+1
            ans=max(ans,r-l+1)
            dic[s[r]]=r
            r+=1
        return ans