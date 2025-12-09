class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9+7
        n = len(nums)
        mv = max(nums)*2
        l,r = [0]*(mv+1),[0]*(mv+1)
        for v in nums:
            r[v]+=1
        ans = 0
        for x in nums:
            r[x]-=1
            t = x*2
            if t<=mv:
                ans = (ans + (l[t]*r[t])%mod)%mod
            l[x]+=1
        return ans%mod