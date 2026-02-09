class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        st = []
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            while st and st[-1]==curr:
                curr+=st[-1]
                st.pop()
            st.append(curr)
        return st