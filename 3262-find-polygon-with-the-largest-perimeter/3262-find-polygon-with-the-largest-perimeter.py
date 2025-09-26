class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        pref =[0]*(n+1)
        for i in range(n):pref[i+1]=nums[i]+pref[i]
        ans = -1
        for i in range(n-1,-1,-1):
            if pref[i]>nums[i]:
                ans = max(pref[i+1],ans)
        return ans