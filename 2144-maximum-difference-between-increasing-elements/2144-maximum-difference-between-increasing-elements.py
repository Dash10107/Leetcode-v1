class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minSoFar = float('inf')
        ans = -1
        for num in nums:
            if minSoFar<num:
                ans = max(num-minSoFar,ans)
            else:
                minSoFar = num
        return ans