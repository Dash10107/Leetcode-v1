class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        mp = {};ans=float('inf')
        def rev(n):
            return int(str(n)[::-1])
        for i,n in enumerate(nums):
            if n in mp:            ans = min(ans,i-mp[n])
            mp[rev(n)]=i
        return ans if ans!=float('inf') else -1