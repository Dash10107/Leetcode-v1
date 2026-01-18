class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        n = len(s)
        c = Counter(s)
        st = []
        for ch in s:
            while st and c[st[-1]]>1 and ch<st[-1]:
                c[st.pop()]-=1
            st.append(ch)
        while c[st[-1]]>1:
            c[st.pop()]-=1
        return ''.join(st)