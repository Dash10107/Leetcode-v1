class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod= 10**9+7
        ans=0;curr=0
        c = defaultdict(int)
        for x,y in points:c[y]+=1
        for p in c.values():
            edge= (p*(p-1))//2
            ans = (ans+edge*curr)%mod
            curr= (curr+edge)%mod
        return ans%mod