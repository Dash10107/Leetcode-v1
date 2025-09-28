class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        s = str(n)
        l = len(s)
        ans = []
        for i in range(l):
            if s[i]!='0':
                th = s[i] + '0'*(l-i-1)
                ans.append(int(th))
        return ans