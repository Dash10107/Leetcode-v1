class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m,o = len(s1),len(s2),len(s3)
        if n+m !=o:
            return False
        dp = {}
        def func(i,j,k):
            if o==k:
                return True
            if (i,j) in dp:
                return dp[(i,j)]
            t = False
            if i<n and s1[i]==s3[k]:
                t = t or func(i+1,j,k+1)
            if j<m and s2[j]==s3[k]:
                t = t or func(i,j+1,k+1)
            dp[(i,j)]=t
            return t
        return func(0,0,0)