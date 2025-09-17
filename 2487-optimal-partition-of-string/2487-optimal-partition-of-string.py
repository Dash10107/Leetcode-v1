class Solution:
    def partitionString(self, s: str) -> int:
        st = set();c=1
        for ch in s:
            if ch in st:
                c+=1
                st.clear()
            st.add(ch)
        return c