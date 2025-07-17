class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        mod = 10**9+7
        heapify(nums)
        while k:
            t = heappop(nums)
            heappush(nums,t+1)
            k-=1
        return prod(nums)% mod