class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0;ones=0;onezero=0
        for ch in s:
            if ch=='1':
                ones+=1
                onezero=1
            elif ch=='0' and onezero==1:
                ans+=ones
                onezero=0
        return ans