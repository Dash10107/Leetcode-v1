class Solution:
    def decodeString(self, s: str) -> str:
        ans = ''
        st = []
        i = 0
        for j in s:
            if j.isdigit():
                i = (i*10)+int(j)
            elif j =='[':
                st.append((ans,i))
                i = 0
                ans=''
            elif j==']':
                val,n=st.pop()
                ans = val + (ans*n)
            else:
                ans+= j
        return ans