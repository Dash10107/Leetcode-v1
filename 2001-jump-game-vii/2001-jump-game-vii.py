class Solution:
    def canReach(self, s: str, minj: int, maxj: int) -> bool:
        if s[-1]=='1':
            return False
        n = len(s)
        end = minj
        ans = [True]+[False]*(n-1)
        for i in range(len(s)):
            if ans[i]:
                start,end= max(i+minj,end),min(i+maxj+1,n)
                for j in range(start,end):
                    if s[j]=='0':
                        ans[j]=True
                if end==n:
                    return ans[-1]
        return ans[-1]
                

