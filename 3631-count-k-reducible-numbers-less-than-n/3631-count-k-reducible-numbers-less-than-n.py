class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        mod = 10**9+7
        cnt = [0]*801
        cnt[1]=1
        for i in range(2,801):
            sb = i.bit_count()
            cnt[i]= 1+cnt[sb]
        @cache
        def func(i,tight,sbits):
            if i==len(s):
                if tight==1 or sbits==0:return 0
                else:return (1 if cnt[sbits]<=k else 0)
            res = 0
            if tight==1:
                if s[i]=='0':
                    res = func(i+1,tight,sbits)
                else:
                    res = (func(i+1,1,sbits+1) +func(i+1,0,sbits))%mod
            else:
                res = (func(i+1,tight,sbits+1) + func(i+1,tight,sbits) )%mod
            return res
        return func(0,1,0)