class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        c = Counter(s)
        if max(c.values())> (n+1)//2:
            return ''
        ans = ['']*n
        chars = sorted(c.items(),key=lambda x:-x[1])
        i=0
        for ch,val in chars:
            while val>0 and i<n:
                ans[i]=ch
                val-=1
                i+=2
            while val>0:
                if i>=n:i=1
                ans[i]=ch
                val-=1
                i+=2
        return ''.join(ans)