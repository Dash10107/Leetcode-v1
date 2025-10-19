class Solution:
    def smallestString(self, s: str) -> str:
        s = list(s)
        i=0;n=len(s)
        while i<n and s[i]=='a':
            i+=1
        if i==n:
            s[-1]='z'
            return ''.join(s)
        while i<n and s[i]!='a':
            s[i]= chr(ord(s[i])-1)
            i+=1
        return ''.join(s)