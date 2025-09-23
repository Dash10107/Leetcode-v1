class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        m = 0;ans=float('-inf')
        for a in arr:
            m+=a
            if m>ans:ans=m
            if m<0:m=0
        return ans