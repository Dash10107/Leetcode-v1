class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9+7
        if n==1:return 1
        b = bin(n)[2:]
        prev = self.concatenatedBinary(n-1)
        prev = ((prev<<len(b))+n)%mod
        return prev