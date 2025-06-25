class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def chk(mid):
            c = 0
            for a in nums1:
                if a>0:
                    c+= bisect_right(nums2,mid//a)
                elif a<0:
                    t = mid//a + (1 if mid%a else 0)
                    c+= n2 - bisect_left(nums2,t)
                else:
                    if mid>=0:
                        c+= n2
            return c

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1        
        n2 = len(nums2)
        lo = min(nums1[0]*nums2[0], nums1[0]*nums2[-1], nums1[-1]*nums2[0], nums1[-1]*nums2[-1])
        hi = max(nums1[0]*nums2[0], nums1[0]*nums2[-1], nums1[-1]*nums2[0], nums1[-1]*nums2[-1])
        while lo<hi:
            mid = (lo+hi)//2
            if chk(mid)>=k:
                hi = mid
            else:
                lo = mid+1
        return lo
