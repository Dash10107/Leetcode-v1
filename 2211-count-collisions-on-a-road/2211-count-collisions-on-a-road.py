class Solution:
    def countCollisions(self, directions: str) -> int:
        st = [];ans=0
        for d in directions:
            if d=='R':st.append(d)
            elif d=='S':
                if st and st[-1]=='R':
                    c=0
                    while st and st[-1]=='R':
                        st.pop()
                        c+=1
                    ans+= c
                st.append(d)
            elif d=='L':
                if st and st[-1]=='R':
                    c=0
                    while st and st[-1]=='R':
                        st.pop()
                        c+=1
                    ans+=(c+1)
                    st.append('S')
                elif st and st[-1]=='S':
                    ans+=1
        return ans