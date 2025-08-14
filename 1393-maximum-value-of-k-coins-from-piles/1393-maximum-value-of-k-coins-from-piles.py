class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        @cache
        def func(p,kk):
            if p==n or kk==0:return 0
            res = func(p+1,kk)
            j =0;curr=0
            while j<len(piles[p]) and j<kk:
                curr+=piles[p][j]
                res = max(res,curr+ func(p+1,kk-j-1))
                j+=1
            return res
        return func(0,k)