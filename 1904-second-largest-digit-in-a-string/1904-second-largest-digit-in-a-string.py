class Solution:
    def secondHighest(self, s: str) -> int:
        st = set()
        for ch in s:
            if ch.isdigit():
                st.add(int(ch))
        if len(st)>=2:
            return sorted(list(st))[-2]
        else:return -1