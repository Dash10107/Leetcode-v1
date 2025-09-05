class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0;carry=0
        for b in range(len(s)-1,0,-1):
            bb = int(s[b])+carry
            if bb%2==0:
                ans+=1
            else:
                ans+=2
                carry=1
        return ans+carry