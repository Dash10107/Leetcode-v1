class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        pref=0
        ans = 0;n=len(nums)
        suff = [0]*(n+1)
        for i in range(n-1,-1,-1):
            suff[i-1]= suff[i]+nums[i]
        for i in range(n-1):
            pref+=nums[i]
            s=suff[i]
            if (pref-s)%2==0:
                ans+=1
        return ans