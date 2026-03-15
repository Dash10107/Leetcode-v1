class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n=len(nums)
        mx=nums[0];pref=[0]*n
        pref[0]=nums[0]
        for i in range(1,n):
            mx = max(nums[i],mx)
            pref[i]= math.gcd(mx,nums[i])
        pref.sort()
        l=0;r=n-1
        ans = 0
        while l<r:
            ans+=math.gcd(pref[l],pref[r])
            l+=1
            r-=1
        return ans