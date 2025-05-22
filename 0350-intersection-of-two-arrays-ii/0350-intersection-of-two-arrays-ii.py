class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums2)
        ans = []
        for n in nums1:
            if n in c and c[n]>0:
                c[n]-=1
                ans.append(n)
        return ans
            