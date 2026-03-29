class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        n = len(nums)
        ans = n+1
        for i in range(n):
            for j in range(i+1,n):
                if (nums[i]==1 and nums[j]==2) or (nums[j]==1 and nums[i]==2):
                    ans = min(ans,abs(i-j))
        return ans if ans!=(n+1) else -1