class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        c1.subtract(c2)
        ans=0
        for ct in c1.values():
            if ct%2:return -1
            ans+=ct if ct>0 else 0
        return ans//2