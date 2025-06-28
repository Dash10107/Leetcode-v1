class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heappush(heap,n)
        while k:
            heappush(heap,-heappop(heap))
            k-=1
        return sum(heap)