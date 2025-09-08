class Solution:
    def smallestNumber(self, num: int) -> int:
        s = str(num)
        if s[0]=='-':
            c = Counter(s[1:])
            ans = ''
            for ch in sorted(c,reverse=True):
                ans+= ch*c[ch]
            return -int(ans)
        else:
            c = Counter(s)
            ans = []
            for ch in sorted(c):
                ans.append(ch*c[ch])
            if '0' in c:
                ans[0] = (ans[1][:1] + ans[0] + ans[1][1:]) if len(ans)>1 else ans[0]
                if len(ans)>1:
                    ans[1]=''
                
            return int(''.join(ans))