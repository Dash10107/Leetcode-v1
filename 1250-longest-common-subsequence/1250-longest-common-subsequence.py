class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        n,m=len(t1),len(t2)
        @cache
        def func(i,j):
            if i==n or j==m:
                return 0
            ans = max(func(i+1,j),func(i,j+1))
            if t1[i]==t2[j]:
                ans = max(ans,1+func(i+1,j+1))
            return ans
        return func(0,0)