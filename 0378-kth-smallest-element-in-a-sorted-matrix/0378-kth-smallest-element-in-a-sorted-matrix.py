class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap =[]
        for i in range(n):
            for j in range(n):
                heappush(heap,matrix[i][j])
        while k-1:
            t = heappop(heap)
            k-=1
        return heappop(heap)