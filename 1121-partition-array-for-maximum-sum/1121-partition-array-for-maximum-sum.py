class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        @lru_cache(None)
        def func(i):
            if i>=n:return 0
            mv,ans = 0,0
            for j in range(i,min(n,i+k)):
                 mv = max(mv,arr[j])
                 ans = max(ans,(j-i+1)*mv+ func(j+1))
            return ans
        return func(0)