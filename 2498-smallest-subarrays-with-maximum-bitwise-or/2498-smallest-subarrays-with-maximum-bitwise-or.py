class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        for i in range(n):
            x = nums[i]
            j = i-1
            ans[i]=1
            while j>=0 and nums[j] | x != nums[j]:
                ans[j]= i-j+1
                nums[j] |= x
                j-=1
        return ans