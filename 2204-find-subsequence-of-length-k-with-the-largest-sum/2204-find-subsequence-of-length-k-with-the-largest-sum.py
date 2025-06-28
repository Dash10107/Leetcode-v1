class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i,n in enumerate(nums):
            heappush(heap,(-n,i))
        ans = []
        while k:
            ans.append(heappop(heap))
            k-=1
        ans.sort(key=lambda x:x[1])
        res = []
        for n,_ in ans:
            res.append(-n)
        return res