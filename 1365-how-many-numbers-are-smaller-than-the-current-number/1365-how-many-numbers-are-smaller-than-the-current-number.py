class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        sortN = sorted(nums)
        for num in nums:
            ans.append(sortN.index(num))
        return ans