class Solution:
    def minimumChairs(self, s: str) -> int:
        ans = 0
        res = 0
        for ch in s:
            if ch=='E':
                ans+=1
            else:
                ans-=1
            res = max(ans,res)
        return res