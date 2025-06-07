class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def func(ind,ind2):
            if ind2>=len(t):
                return 1 
            if ind>=len(s):
                return 0
            notTake = func(ind+1,ind2)
            take = 0
            if s[ind]==t[ind2]:
                take+=func(ind+1,ind2+1)
            return take + notTake
        return func(0,0)
    