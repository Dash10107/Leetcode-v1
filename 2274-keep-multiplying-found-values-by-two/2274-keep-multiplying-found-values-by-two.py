class Solution:
    def findFinalValue(self, a: List[int], v: int) -> int:
        return v in a and self.findFinalValue(a,2*v) or v