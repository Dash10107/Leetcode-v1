class Solution:
    def canIWin(self, maxi: int, total: int) -> bool:
        r = list(range(1,maxi+1))
        s = sum(r)
        if s<=0:
            return True
        if s<total:
            return False
        @cache
        def func(avail,t):
            if avail[-1]>=t:
                return True
            for i in range(len(avail)):
                if not func(avail[:i]+avail[i+1:],t-avail[i]):
                    return True
            return False
        return func(tuple(r),total)