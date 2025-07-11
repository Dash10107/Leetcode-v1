class Solution:
    def minMoves(self, heap: List[int]) -> int:
        return sum(heap)-len(heap)*min(heap)