class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        st = []
        ans = []
        for h in heights[::-1]:
            c = 0
            while st and st[-1]<h:
                st.pop()
                c+=1
            if st:
                c+=1
            ans.append(c)
            st.append(h)
        return ans[::-1]
