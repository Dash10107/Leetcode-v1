class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        st = str(start-1);fin = str(finish)
        dp = {}
        def func(num,tight,n):
            if len(num)<len(s):return 0
            if (n,tight) in dp:return dp[(n,tight)]
            ub = (int(num[len(num)-n]) if tight else limit)
            ans = 0
            if n==1:
                a = int(s[len(s)-n])
                if a>ub:return 0
                else:return 1
            if n<=len(s):
                if tight:
                    a = int(s[len(s)-n])
                    if a>ub:return 0
                    elif a==ub:
                        ans += func(num,True,n-1)
                        return ans
                    else:
                        return 1
                else:
                    return 1
            else:
                i=0
                while i<=ub and i<=limit:
                    ans += func(num,tight and (i==ub),n-1)
                    i+=1
            dp[(n,tight)]=ans
            return ans
        a= func(fin,True,len(fin))
        dp  = {}
        b = func(st,True,len(st))
        return a-b