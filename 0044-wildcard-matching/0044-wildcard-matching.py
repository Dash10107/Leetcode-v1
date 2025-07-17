class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n=len(s);m = len(p)
        if p=='*':
            return True
        dp ={}
        def func(i,j):
            if i==n and j==m:
                return True
            if j==m:
                return False
            if i==n:
                while j < m and p[j] == '*':
                    j += 1
                return j == m
            if (i,j) in dp:
                return dp[(i,j)]
            t = False
            if s[i]==p[j] or p[j]=='?':
                t = t or func(i+1,j+1)
            elif p[j]=='*':
                t = t or func(i+1,j) or func(i,j+1)
            dp[(i,j)]=t
            return t
        return func(0,0)