class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0]*(n+1)
        for i in range(n):
            pref[i+1]=pref[i]+nums[i]
        m = min(pref[1:])
        if m>=1:return 1
        else:
            return (-m)+1