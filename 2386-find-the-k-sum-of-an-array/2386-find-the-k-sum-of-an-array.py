class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        ms = sum([max(0,num) for num in nums])
        absn = sorted([abs(num) for num in nums])
        heap = [(-ms+absn[0],0)]
        ans = [ms]
        while len(ans)<k:
            nxt,i = heappop(heap)
            heappush(ans,-nxt)
            if i+1<len(absn):
                heappush(heap,(nxt-absn[i]+absn[i+1],i+1))
                heappush(heap,(nxt+absn[i+1],i+1))
        return ans[0]