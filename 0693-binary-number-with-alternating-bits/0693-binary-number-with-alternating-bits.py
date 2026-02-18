class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        curr = n&1
        n>>=1
        while n:
            if curr == n&1:return False
            curr = n&1
            n>>=1
        return True