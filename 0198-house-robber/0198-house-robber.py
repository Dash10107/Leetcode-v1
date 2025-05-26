class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[0]
        prev2 = 0
        for i in range(1,n):
            take = nums[i]
            if i >1 : take+=prev2
            notTake = 0 + prev
            curr = max(take,notTake)
            prev2 = prev
            prev = curr
        return prev
        