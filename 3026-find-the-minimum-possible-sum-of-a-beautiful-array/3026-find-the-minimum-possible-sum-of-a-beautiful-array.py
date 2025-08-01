class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        k = min(n,target//2)
        s1 = k*(k+1)//2
        s2 = (n-k)*(2* target + (n-k-1)) //2
        return (s1+s2)%(10**9+7)