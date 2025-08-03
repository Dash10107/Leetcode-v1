class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10**9+7
        heap = []
        ans = 0
        engs = sorted(zip(efficiency,speed),reverse=True)
        curr = 0
        for ceff,cspee in engs:
            curr+= cspee
            heappush(heap,cspee)
            if len(heap)>k:
                curr-=heappop(heap)
            ans = max(ans,curr*ceff)
        return ans%mod