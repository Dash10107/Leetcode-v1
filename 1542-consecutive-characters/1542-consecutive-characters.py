class Solution:
    def maxPower(self, s: str) -> int:
        c='#';curr=0;ans=0
        for ch in s:
            if c==ch:
                curr+=1
            else:
                c = ch
                curr=1
            ans=max(ans,curr)
        return ans