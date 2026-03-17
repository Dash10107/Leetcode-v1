class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        
        l, h = 0, n
        total_left = (n + m + 1) // 2
        while l <= h:
            m1 = (l + h) // 2
            m2 = total_left - m1

            l1 = nums1[m1 - 1] if m1 > 0 else float('-inf')
            l2 = nums2[m2 - 1] if m2 > 0 else float('-inf')
            r1 = nums1[m1] if m1 < n else float('inf')
            r2 = nums2[m2] if m2 < m else float('inf')

            if l1 <= r2 and l2 <= r1:
                if (n + m) % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                h = m1 - 1
            else:
                l = m1 + 1

        return 0  
