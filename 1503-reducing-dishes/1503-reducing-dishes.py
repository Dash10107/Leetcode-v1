class Solution:
    def maxSatisfaction(self, sat: List[int]) -> int:
        sat.sort()
        n = len(sat)
        @cache
        def func(i,c):
            if i==n:
                return 0
            nottake = func(i+1,c)
            take = sat[i]*c + func(i+1,c+1)
            return max(nottake,take)
        return func(0,1)