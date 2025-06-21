class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        ch = sorted(c.values(),reverse=True)
        st = set()
        ans =0
        for i in range(len(ch)):
            if ch[i] in st:
                while ch[i]!=0 and  ch[i] in st:
                    ch[i]-=1
                    ans+=1
                st.add(ch[i])
            else:
                st.add(ch[i])

        return ans