class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        mod = 10**9+7
        if k==0:return 2
        ans = comb(n-1,k)%mod
        ans = (ans*2)%mod
        return ans