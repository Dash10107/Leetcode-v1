class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        c = 0
        i=0
        res = []
        for j,ch in enumerate(s):
            if ch=='1':c+=1
            else:c-=1
            if c==0:
                m = self.makeLargestSpecial(s[i+1:j])
                res.append('1'+m+'0')
                i=j+1
        res.sort(reverse=True)
        return ''.join(res)