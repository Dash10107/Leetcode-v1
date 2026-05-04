class Solution:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def func(x,jump,down):
            if x>k+1:return 0   
            ans=0
            if x==k:ans+=1
            ans+=func(x+pow(2,jump),jump+1,False)
            if not down and x:ans+=func(x-1,jump,True)
            return ans
        return func(1,0,False)