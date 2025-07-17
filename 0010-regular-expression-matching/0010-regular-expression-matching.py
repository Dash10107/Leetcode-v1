class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        n,m = len(s),len(p)
        def func(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if j==m:
                return i==n
            f = i<n and (s[i]==p[j] or p[j]=='.')
            if j+1<m and p[j+1]=='*':
                dp[(i,j)] =  func(i,j+2) or  (f and  func(i+1,j))
            else:
                dp[(i,j)] = f and func(i+1,j+1)
            return dp[(i,j)]
        return func(0,0)
                
