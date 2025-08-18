class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n = len(s);m=len(t)
        k =m-1;j=m-1
        dp = [-1]*m
        for i in range(n-1,-1,-1):
            if j>=0 and s[i]==t[j]:
                dp[k]=i
                j-=1
                k-=1
        ans = k+1;jj=0
        if ans==0:return 0
        for ii in range(n):
            if jj<m and t[jj]==s[ii]:
                while k<m and dp[k]<=ii:
                    k+=1
                ans = min(ans,k-jj-1)
                jj+=1
        return ans