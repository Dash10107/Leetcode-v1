class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        mod = 10**9+7
        ans=[];n=len(nums1)
        heap=[]
        for i in range(n):
            ones = nums1[i];zeros = nums0[i]
            if zeros==0:
                ans.append('1'*ones)
                continue
            heappush(heap,(-ones,zeros))
        while heap:
            ones,zeros=heappop(heap)
            ones=-ones
            ans.append('1'*ones+'0'*zeros)
        return int(''.join(ans),2)%mod