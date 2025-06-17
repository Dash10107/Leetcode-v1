class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        snums1 = set(nums1)
        snums2 = set(nums2)
        temp1 = list(snums1-snums2)
        temp2 = list(snums2-snums1)
        return [temp1,temp2]