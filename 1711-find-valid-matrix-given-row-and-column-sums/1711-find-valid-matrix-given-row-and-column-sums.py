class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum);m=len(colSum)
        ans = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j]=min(rowSum[i],colSum[j])
                rowSum[i]-=ans[i][j]
                colSum[j]-=ans[i][j]
        return ans