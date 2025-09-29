class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def func(i,j):
            if i+2>j:return 0
            if i+2==j:return values[i]*values[i+1]*values[j]
            ans = float('inf')
            for k in range(i+1,j):
                ans = min(ans,values[i]*values[k]*values[j] + func(i,k)+func(k,j))
            return ans
        return func(0,len(values)-1)