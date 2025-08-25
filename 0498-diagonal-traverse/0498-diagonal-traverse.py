class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        n = len(mat);m=len(mat[0])
        for i in range(n):
            for j in range(m):
                g[i+j].append(mat[i][j])
        ans = []
        for i in range(m+n-1):
            if i%2==0:
                ans+= g[i][::-1]
            else:
                ans+= g[i]
        return ans