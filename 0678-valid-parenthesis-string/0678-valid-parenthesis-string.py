class Solution:
    def checkValidString(self, s: str) -> bool:
        st = []
        star = []
        for i,ch in enumerate(s):
            if ch=='(':
                st.append(i)
            elif ch==')':
                if st:
                    st.pop()
                elif star:
                    star.pop()
                else:
                    return False
            elif ch=='*':
                star.append(i)
        while st and star:
            if st[-1]>star[-1]:
                return False
            st.pop()
            star.pop()
        return len(st)==0