class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9+7
        curr=0;ans=0
        for ch in s:
            if ch=='1':
                curr+=1
            else:curr=0
            ans+=curr
        return ans%mod