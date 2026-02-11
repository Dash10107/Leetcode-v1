class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n,m = len(s),len(t)
        dp0 = [[0]*(m+1) for _ in range(n+1)]
        dp1 = [[0]*(m+1) for _ in range(n+1)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if s[i]==t[j]:
                    dp0[i+1][j+1] = 1 + dp0[i][j]
                    dp1[i+1][j+1]= dp1[i][j]
                else:
                    dp0[i+1][j+1]=0
                    dp1[i+1][j+1]=dp0[i][j]+1
                ans+=dp1[i+1][j+1]
        return ans
