class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0;n=len(nums)
        i=0;zer = 0
        for j in range(n):
            if nums[j]==0:
                zer+=1
            while zer>1:
                if nums[i]==0:
                    zer-=1
                i+=1
            ans = max(ans,j-i)
        return ans