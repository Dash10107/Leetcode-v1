class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        s = list(s)
        l,r = 0,n-1
        while l<=r:
            if s[l]=='1':l+=1
            if s[r]=='0':r-=1
            if l<=r and s[l]=='0' and s[r]=='1':
                s[l],s[r]=s[r],s[l]
        s[l-1],s[n-1]=s[n-1],s[l-1]
        return ''.join(s)