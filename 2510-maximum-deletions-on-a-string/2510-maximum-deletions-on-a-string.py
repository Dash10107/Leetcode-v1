class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        dp = [1]*n
        if len(set(s))==1:
            return n
        for i in range(n-2,-1,-1):
            for l in range(1,(n-i)):
                if s[i:i+l]==s[i+l:i+2 * l]:
                    dp[i]=max(dp[i],1+dp[i+l])
        return dp[0]