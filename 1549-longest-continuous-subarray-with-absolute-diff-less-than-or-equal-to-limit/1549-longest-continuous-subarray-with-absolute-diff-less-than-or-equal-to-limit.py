class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        maheap,miheap = [],[]
        ans = 0
        for r in range(len(nums)):
            heapq.heappush(maheap,(-nums[r],r))
            heapq.heappush(miheap,(nums[r],r))
            while -maheap[0][0] - miheap[0][0]>limit:
                left = min(maheap[0][1],miheap[0][1])+1
                while miheap[0][1]<left:
                    heapq.heappop(miheap)
                while maheap[0][1]<left:
                    heapq.heappop(maheap)
            ans = max(ans,r-left+1)
        return ans