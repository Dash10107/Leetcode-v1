class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        res = [0]*n
        if k==0:return res
        s = 1;e = k;t = 0
        if k<0:
            s = n-abs(k)
            e = n-1
        t = sum(code[s:e+1])
        for i in range(n):
            res[i]=t
            t-= code[s%n]
            t+= code[(e+1) %n]
            s+=1
            e+=1
        return res