class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        mod=10**9+7
        for i in range(n):
            
            t1,t2=a^(1<<i),b^(1<<i)
            
            if t1*t2>a*b:
                a,b=t1,t2
        return (a*b)%mod