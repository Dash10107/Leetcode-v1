class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        mod = 10**9+7
        def count(x):
            @lru_cache(None)
            def dp(pos,last,tight,start):
                if pos==len(x):
                    return 1 if start else 0
                lim = int(x[pos]) if tight else 9
                res = 0
                for d in range(0,lim+1):
                    ntight = tight and (d==lim)
                    if not start:
                        if d==0:
                            res+=dp(pos+1,-1,ntight,False)
                        else:
                            res+=dp(pos+1,d,ntight,True)
                    else:
                        if abs(d-last)==1:
                            res+=dp(pos+1,d,ntight,True)
                return res%mod
            return dp(0,-1,True,False)
        return (count(high)-count(str(int(low)-1)))%mod