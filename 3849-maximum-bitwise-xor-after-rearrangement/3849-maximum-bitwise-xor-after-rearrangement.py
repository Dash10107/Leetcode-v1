class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        t = Counter(t)
        ans='';n=len(s)
        for i in range(n):
            pos = n-1-i
            if s[i]=='1':
                if t['0']>=1:
                    ans+='1'
                    t['0']-=1
                else:
                    ans+='0'
                    t['1']-=1
            else:
                if t['1']>=1:
                    ans+='1'
                    t['1']-=1
                else:
                    ans+='0'
                    t['0']-=1
        return ans