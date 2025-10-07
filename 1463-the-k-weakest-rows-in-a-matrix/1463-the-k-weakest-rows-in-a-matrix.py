class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i in range(len(mat)):
            s = sum(mat[i])
            heappush(heap,(s,i))
        ans = []
        while k:
            ans.append(heappop(heap)[1])
            k-=1
        return ans
