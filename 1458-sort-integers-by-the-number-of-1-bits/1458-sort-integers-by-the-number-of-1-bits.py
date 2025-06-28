class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        temp = []
        for n in arr:
            b = bin(n)[2:].count('1')
            temp.append((b,n))
        temp.sort()
        return [t[1] for t in temp]