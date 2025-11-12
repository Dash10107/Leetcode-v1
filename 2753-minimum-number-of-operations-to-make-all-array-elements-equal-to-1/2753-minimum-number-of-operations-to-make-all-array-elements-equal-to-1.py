class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dist = float("inf")
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i + 1, len(nums)):
                if gcd(curr, nums[j]) == 1:
                    dist = min(dist, j - i)
                    break
                curr = gcd(curr, nums[j])
           
        if dist == float("inf"):
            return -1
        return len(nums) + dist - 1 - nums.count(1)