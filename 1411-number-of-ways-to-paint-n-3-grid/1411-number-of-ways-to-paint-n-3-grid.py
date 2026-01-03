class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9+7
        aba= 6;abc=6
        for _ in range(n-1):
            naba = (3*aba + 2*abc)%mod
            nabc = (2*aba + 2*abc)%mod
            aba = naba
            abc = nabc
        return (aba+abc)%mod