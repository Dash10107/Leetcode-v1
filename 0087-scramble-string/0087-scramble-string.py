class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n!=len(s2):
            return False
        @cache
        def func(i,j,l):
            if s1[i:i+l]==s2[j:j+l]:
                return True
            if Counter(s1[i:i+l])!=Counter(s2[j:j+l]):
                return False
            for k in range(1,l):
                if func(i,j,k) and func(i+k,j+k,l-k):
                    return True
                if func(i+k,j,l-k) and func(i,j+l-k,k):
                    return True
            return False
        return func(0,0,n)