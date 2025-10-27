class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        rows = []
        for b in bank:
            c=b.count('1')
            if c:rows.append(c)
        if len(rows)<=1:return 0
        ans = 0
        for i in range(len(rows)-1):
            a = rows[i]*rows[i+1]
            ans+=a
        return ans