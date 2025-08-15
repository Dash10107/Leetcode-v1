class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod =10**9+7
        dp = defaultdict(int)
        dp[(0,0)]=1
        for i in range(1,n+1):
            for j in range(k+1):
                if j==0:
                    dp[(i,j)]=1
                    continue
                dp[(i,j)] = (dp[(i-1,j)] + dp[(i,j-1)])%mod
                if j>=i:
                    dp[(i,j)] = (dp[(i,j)]-dp[(i-1,j-i)]+mod)%mod
        return dp[(n,k)]