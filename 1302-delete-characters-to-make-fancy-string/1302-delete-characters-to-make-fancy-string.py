class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        ans='';i=0
        while i<n:
            t = s[i]
            j = i;c=1
            while j<n and t==s[j]:
                j+=1
            if j-i>=3:
                ans+= t*2
            else:
                ans+= t*(j-i)
            i = j
        return ans