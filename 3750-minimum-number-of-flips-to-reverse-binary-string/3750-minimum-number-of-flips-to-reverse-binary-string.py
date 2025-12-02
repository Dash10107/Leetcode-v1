class Solution:
    def minimumFlips(self, n: int) -> int:
        s = bin(n)[2:]
        c = 0
        for a,b in zip(s[::-1],s):
            if a!=b:c+=1
        return c