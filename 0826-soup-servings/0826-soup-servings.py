class Solution:
    def soupServings(self, n: int) -> float:
        if n>5000:
            return 1.0
        u = math.ceil(n/25)
        @lru_cache(None)
        def func(a,b):
            if a<=0 and b<=0:
                return 0.5
            if a<=0:
                return 1.0
            if b<=0:
                return 0.0
            return 0.25*(
                func(a-4,b)+
                func(a-3,b-1)+
                func(a-2,b-2)+
                func(a-1,b-3)
            ) 
        return func(u,u)