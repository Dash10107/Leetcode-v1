class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        m = max(nums)
        nums = set(nums)
        i=1
        while k*i<=m:
            if k*i not in nums:
                break
            else:
                i+=1
        return k*i