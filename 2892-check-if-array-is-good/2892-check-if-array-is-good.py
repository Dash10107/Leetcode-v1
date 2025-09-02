class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m = max(nums)
        return sorted(nums)== list(range(1,m+1))+[m]