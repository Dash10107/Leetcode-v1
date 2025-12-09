class Solution:
    def numberOfWays(self, s: str) -> int:
        zer=0;one=0;ans=0
        tot0=s.count('0')
        tot1=len(s)-tot0
        for ch in s:
            if ch=='1':
                tot1-=1
                ans+=(zer*tot0)
                one+=1
            else:
                tot0-=1
                ans+=(one*tot1)
                zer+=1
        return ans