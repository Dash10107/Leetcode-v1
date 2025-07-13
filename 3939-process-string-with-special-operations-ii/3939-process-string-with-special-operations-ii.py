class Solution:
    def processStr(self, s: str, k: int) -> str:
        cl = 0
        for ch in s:
            if ch.islower():
                cl += 1
            elif ch == '*':
                if cl > 0:
                    cl -= 1
            elif ch == '#':
                cl *= 2
        if k >= cl:
            return '.'
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch.islower():
                if k == cl - 1:
                    return ch
                cl -= 1
            elif ch == '*':
                cl += 1
            elif ch == '#':
                cl //= 2
                if k >= cl:
                    k -= cl
            elif ch == '%':
                k = cl - 1 - k
        return '.'
