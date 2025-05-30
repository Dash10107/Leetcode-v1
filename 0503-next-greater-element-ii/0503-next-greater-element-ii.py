class Solution:
    def nextGreaterElements(self, nums1: List[int]) -> List[int]:
        n = len(nums1)
        nums2 = nums1 + nums1
        res = [-1] * n
        st = deque()

        for i in range(2 * n - 1, -1, -1):
            while st and st[-1] <= nums2[i]:
                st.pop()
            if i < n:
                if st:
                    res[i] = st[-1]
            st.append(nums2[i])
        
        return res