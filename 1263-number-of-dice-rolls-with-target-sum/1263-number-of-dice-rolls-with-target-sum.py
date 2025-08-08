class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9+7
        @lru_cache(None)
        def func(i,s):
            if i==n: return (1 if s==target else 0)
            if i>n:return 0
            c=0
            for j in range(1,k+1):
                if j+s<=target:
                    c+= (func(i+1,j+s)%mod)
            return (c%mod)
        return (func(0,0)%mod)