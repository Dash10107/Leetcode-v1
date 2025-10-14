class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:heappush(heap,-stone)
        ans = 0
        while len(heap)>1:
            stone = -heappop(heap)
            stone2 = -heappop(heap)
            if stone!=stone2:
                heappush(heap,-abs(stone-stone2))
        return abs(heap[0]) if heap else 0