class Solution:
    def myAtoi(self, s: str) -> int:
        neg = False
        t = 0
        s = s.lstrip()
        if s and s[0]=='-':
            neg=True
            s = s[1:]
        elif s and s[0]=='+':
            s = s[1:]
        for ch in s:
            if ch not in '0123456789':
                break
            else:
                t = t*10 + int(ch)
        m = 2**31-1
        if not neg and  t>m:
            return m
        if neg and t>m:
            return -(m+1)
        return -t if neg else t