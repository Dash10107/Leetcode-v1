class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = [ele for ele in nums if ele!=0]
        return len(set(nums))