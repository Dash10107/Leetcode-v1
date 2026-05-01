class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        n = str(n);x=str(x)
        return (not (n.startswith(x))) and (x in n)