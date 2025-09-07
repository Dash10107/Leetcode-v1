class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        return 1 if len(c.keys())!=1 else 0