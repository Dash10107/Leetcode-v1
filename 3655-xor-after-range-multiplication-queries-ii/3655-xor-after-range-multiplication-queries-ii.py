class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9+7;n=len(nums)
        b = int(n**0.5)
        groups = [[] for _ in range(b)]
        for l,r,k,v in queries:
            if k<b:
                groups[k].append((l,r,v))
            else:
                for i in range(l,r+1,k):
                    nums[i]=(nums[i]*v)%mod
        diff = [1]*(n+b)
        for k in range(1,b):
            if not groups[k]:continue
            diff[:]= [1]*len(diff)
            for l,r,v in groups[k]:
                diff[l]=(diff[l]*v)%mod
                last = ((r-l)//k+1)*k+l
                diff[last]=diff[last]* pow(v,mod-2,mod)%mod
            for i in range(k,n):
                diff[i]=(diff[i]*diff[i-k])%mod
            for i in range(n):
                nums[i]=(nums[i]*diff[i])%mod
        ans = 0
        for nn in nums:
            ans^=nn
        return ans