class Solution:
    def maxSum(self, nums: List[int]) -> int:
        c = Counter(nums)
        m  = max(nums)
        if len(nums)==1:
            return nums[0]
        elif m<0:
            return m  
        ans = 0
        for ch in c:
            if c[ch]>=1 and ch>0:
                ans+= ch
        return ans