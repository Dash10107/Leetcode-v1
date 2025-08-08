class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        suffix = [0]*n
        suffix[n-1]=piles[n-1]
        for i in range(n-2,-1,-1):suffix[i]=piles[i]+suffix[i+1]
        @lru_cache(None)
        def func(i,m):
            if i==n:return 0
            if i+2*m>=n:return suffix[i]
            ans = float('-inf')
            for j in range(1,2*m+1):
                ans = max(ans,suffix[i]-func(i+j,max(m,j)))
            return ans
        return func(0,1)
        