class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        ans = 0;count = 0
        for n in nums:
            ans^=n
            count+=(1 if n==0 else 0)
        n = len(nums)
        if ans==0:return n-1 if count!=n else 0
        return n