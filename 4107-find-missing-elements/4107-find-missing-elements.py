class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mi = min(nums);ma=max(nums)
        nums = set(nums);ans=[]
        for i in range(mi,ma+1):
            if i not in nums:ans.append(i)
        return ans