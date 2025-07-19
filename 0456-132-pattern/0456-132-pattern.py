class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        st = []
        if len(nums)<3:
            return False
        s3 = float('-inf')
        for n in reversed(nums):
            if n<s3:
                return True
            while st and st[-1]<n:
                s3 = st.pop()
            st.append(n)
        return False