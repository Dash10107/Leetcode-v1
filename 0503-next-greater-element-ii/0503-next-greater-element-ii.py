class Solution:
    def nextGreaterElements(self, nums1: List[int]) -> List[int]:
        n = len(nums1)
        res = [-1] * n
        st = deque()

        for i in range(2 * n - 1, -1, -1):
            cur = nums1[i % n]
            while st and nums1[st[-1]] <= cur:
                st.pop()
            if st:
                res[i % n] = nums1[st[-1]]
            st.append(i % n)

        return res