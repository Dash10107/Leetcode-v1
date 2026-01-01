class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int(''.join(str(x) for x in digits))
        n+=1
        return list(map(int,str(n)))