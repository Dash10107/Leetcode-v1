class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        dic  = defaultdict(int)
        i = 0
        for j in range(len(s)):
            if dic[s[j]]>0:
                i = max(dic[s[j]],i)
            ans = max(ans,j-i+1)
            dic[s[j]] = j+1
        return ans
            