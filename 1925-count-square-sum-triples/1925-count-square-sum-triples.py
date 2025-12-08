class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1,n+1):
            p = i**2
            for j in range(i+1,n+1):
                q = j**2
                r = sqrt(p+q)
                if r<=n and r==int(r) :
                    ans+=2
        return ans