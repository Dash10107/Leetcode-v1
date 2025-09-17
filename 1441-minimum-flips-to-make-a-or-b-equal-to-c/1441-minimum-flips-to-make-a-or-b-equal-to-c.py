class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a>0 or b>0 or c>0:
            ba,bb,bc = a&1,b&1,c&1
            if bc == 0:
                ans+= (ba+bb)
            else:
                ans+= (1 if ba==0 and bb==0 else 0)
            a,b,c = a>>1,b>>1,c>>1
        return ans