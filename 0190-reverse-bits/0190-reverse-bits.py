class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            b = n&1
            res = (res<<1)|b
            n>>=1
        return res 