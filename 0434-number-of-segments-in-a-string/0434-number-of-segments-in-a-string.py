class Solution:
    def countSegments(self, s: str) -> int:
        ans = 0
        i=0
        while i<len(s):
            if s[i]!=' ':
                j = i
                while j<len(s) and  s[j]!=' ':
                    j+=1
                ans+=1
                i = j
            else:
                i+=1
        return ans

                