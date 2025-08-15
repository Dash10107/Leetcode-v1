class Solution:
    def isScramble(self, s: str, t: str) -> bool:
        d = {}
        def func(s1,s2):
            n = len(s1)
            if s1==s2:return True
            if n==1:return False
            key = s1+s2
            if key in d:return d[key]
            for i in range(1,n):
                if func(s1[:i],s2[:i]) and func(s1[i:],s2[i:]):
                    d[key]=True
                    return True
                if func(s1[:i],s2[-i:]) and func(s1[i:],s2[:-i]):
                    d[key]=True
                    return True
            d[key]=False
            return False
        return func(s,t)