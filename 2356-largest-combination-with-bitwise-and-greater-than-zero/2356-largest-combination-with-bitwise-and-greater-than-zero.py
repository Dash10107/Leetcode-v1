class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bits = [0]*24
        for n in candidates:
            for i in range(24):
                if n & (1<<i):
                    bits[i]+=1
        return max(bits)