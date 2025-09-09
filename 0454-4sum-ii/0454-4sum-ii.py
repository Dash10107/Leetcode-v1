class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum12 = Counter(a + b for a in nums1 for b in nums2)
        ans = 0
        for c in nums3:
            for d in nums4:
                t = -(c+d)
                if t in sum12:ans+=sum12[t]
        return ans