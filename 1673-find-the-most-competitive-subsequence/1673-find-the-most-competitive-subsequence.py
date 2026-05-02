class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        st=[]
        extra = len(nums)-k
        for num in nums:
            while st and extra and st[-1]>num:
                st.pop()
                extra-=1
            st.append(num)
        return st[:k]