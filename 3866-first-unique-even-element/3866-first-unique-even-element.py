class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        c = Counter(nums)
        for val in nums:
            if val%2==0 and c[val]==1:
                return val
        return -1