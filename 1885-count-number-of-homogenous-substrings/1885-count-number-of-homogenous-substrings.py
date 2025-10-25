class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9+7
        n = len(s);ans=0;i=0
        while i<n:
            ch = s[i]
            c = 0
            while i<n and s[i]==ch:
                i+=1
                c+=1
            ans= (ans+ ((c*(c+1))//2)%mod)%mod
        return ans
            