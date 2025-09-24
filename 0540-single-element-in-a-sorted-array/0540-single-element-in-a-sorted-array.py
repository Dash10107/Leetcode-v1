class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        xor = 0
        for a in arr:
            xor^=a
        return xor