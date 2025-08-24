class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ans=0;i=0;zero=0
        for j in range(n):
            if nums[j]==0:
                zero+=1
            while zero>k:
                if nums[i]==0:
                    zero-=1
                i+=1
            ans = max(ans,j-i+1)
        return ans