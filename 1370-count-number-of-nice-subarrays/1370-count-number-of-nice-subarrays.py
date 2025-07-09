class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [nums[i]%2 for i in range(len(nums))]
        c = {0:1}
        ans = 0
        curr = 0
        for num in nums:
            curr+=num
            if curr-k in c:
                ans+= c[curr-k]
            c[curr]= c.get(curr,0)+1
        return ans