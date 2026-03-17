class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        op=0
        for ch in s:
            if ch=='(':
                op+=1
                res.append(ch)
            elif ch==')':
                if op>0:
                    op-=1
                    res.append(ch)
            else:res.append(ch)
        final = []
        for ch in reversed(res):
            if ch=='(' and op>0:
                op-=1
                continue
            final.append(ch)
        return ''.join(reversed(final))