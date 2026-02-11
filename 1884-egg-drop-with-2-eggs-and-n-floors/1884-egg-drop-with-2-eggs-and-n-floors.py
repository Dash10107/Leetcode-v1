class Solution:
    def twoEggDrop(self, n: int) -> int:
        return math.ceil((math.sqrt(1 + 8*n) - 1) / 2)