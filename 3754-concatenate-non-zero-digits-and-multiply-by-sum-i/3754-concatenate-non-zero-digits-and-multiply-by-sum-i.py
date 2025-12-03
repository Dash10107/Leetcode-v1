class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ''
        for i in str(n):
            if i!='0':x+=str(i)
        s = sum(int(i) for i in x)
        x=int(x) if x else 0
        return s*x