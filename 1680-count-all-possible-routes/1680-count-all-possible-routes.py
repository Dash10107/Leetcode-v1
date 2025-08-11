class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9+7;n = len(locations)
        @lru_cache(None)
        def func(i,fuel):
            if fuel<0:return 0
            ans = 0
            if i==finish:ans+=1
            for j in range(n):
                l = locations[j]
                if j!=i and abs(l-locations[i])<=fuel:
                    ans+= func(j,fuel-abs(l-locations[i]))
                    ans %= mod
            return ans
        return func(start,fuel)