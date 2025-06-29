class Solution:
    def partitionString(self, s: str) -> List[str]:
        ans = set()
        res = []
        st = ''
        for i in range(len(s)):
            st += s[i]
            if st not in ans:
                ans.add(st)
                res.append(st)
                st=''
        return res