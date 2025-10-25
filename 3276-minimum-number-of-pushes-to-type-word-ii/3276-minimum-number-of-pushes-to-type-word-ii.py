class Solution:
    def minimumPushes(self, word: str) -> int:
        c=Counter(word)
        s = sorted(c.values(),reverse=True)
        ans=0;ct=0
        for p in s:
            ct+=1
            if ct<=8:ans+= (1*p)
            elif ct<=16:ans+= (2*p)
            elif ct<=24:ans+= (3*p)
            else:ans+= (4*p)
        return ans