class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        mod = 10**9+7
        prev = [1]*(k+1);curr = [1]*(k+1) 
        for i in range(1,n):
            for j in range(1,k+1):
                curr[j]= (prev[j]+curr[j-1])%mod
            prev = curr
        return curr[k]