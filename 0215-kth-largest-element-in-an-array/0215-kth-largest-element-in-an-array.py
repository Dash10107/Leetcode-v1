class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heappush(heap,-n)
        t = 0
        while k:
            t = -heappop(heap)
            k-=1
        return t