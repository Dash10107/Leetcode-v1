class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        r = s%p
        if r==0:return 0
        mp = {0:-1}
        pref = 0;n=len(nums);ans=n
        for i,v in enumerate(nums):
            pref = (pref+v)%p
            targ = (pref-r)%p
            if targ in mp:
                ans = min(ans,i-mp[targ])
            mp[pref]=i
        return ans if ans<n else -1 