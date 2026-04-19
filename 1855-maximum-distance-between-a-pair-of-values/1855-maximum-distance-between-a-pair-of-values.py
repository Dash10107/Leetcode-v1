class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i=0;j=0
        while i<len(nums1) and j<len(nums2):
            i+=(nums1[i]>nums2[j])
            j+=1
        return max(0,j-i-1)