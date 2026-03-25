class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        fixed=0;isok=True
        for i in range(n):
            if nums1[i]<=nums1[n-1] and nums2[i]<=nums2[n-1]:
                continue
            elif nums2[i]<=nums1[n-1] and nums1[i]<=nums2[n-1]:
                fixed+=1
            else:
                isok=False
                break
        swapped=1;isok=True
        nums1[n-1],nums2[n-1]=nums2[n-1],nums1[n-1]
        for i in range(n):
            if nums1[i]<=nums1[n-1] and nums2[i]<=nums2[n-1]:
                continue
            elif nums2[i]<=nums1[n-1] and nums1[i]<=nums2[n-1]:
                swapped+=1
            else:
                isok=False
                break
        if not isok:return -1
        return min(fixed,swapped)