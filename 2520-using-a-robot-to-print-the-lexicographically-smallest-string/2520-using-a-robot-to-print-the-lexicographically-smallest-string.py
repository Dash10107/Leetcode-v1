class Solution:
    def robotWithString(self, s: str) -> str:
        suff = ['']*len(s)
        suff[-1]=s[-1]
        for i in range(len(s)-2,-1,-1):
            if suff[i+1]<s[i]:
                suff[i]=suff[i+1]
            else:
                suff[i]=s[i]
        t,ans,i = [],[],0
        while i<len(s):
            while t and t[-1]<=suff[i]:
                ans.append(t.pop())
            t.append(s[i])
            i+=1
        while t:
            ans.append(t.pop())
        return ''.join(ans)