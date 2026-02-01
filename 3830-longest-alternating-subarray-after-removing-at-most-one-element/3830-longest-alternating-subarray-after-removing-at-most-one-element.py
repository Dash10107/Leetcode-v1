class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        u,d = [1]*n,[1]*n
        u1,d1 = [1]*n,[1]*n
        ans = 1
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                u[i]=max(u[i],d[i-1]+1)
                u1[i]=max(u1[i],d1[i-1]+1)
            elif nums[i]<nums[i-1]:
                d[i]=max(d[i],u[i-1]+1)
                d1[i]=max(d1[i],u1[i-1]+1)
            if i>=2 and nums[i]>nums[i-2]:
                u1[i]=max(u1[i],d[i-2]+1)
            elif i>=2 and nums[i]<nums[i-2]:
                d1[i]=max(d1[i],u[i-2]+1)
            ans = max(ans,u[i],d[i],u1[i],d1[i])
        return ans