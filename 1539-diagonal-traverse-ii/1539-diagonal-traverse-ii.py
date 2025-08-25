class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        n = len(mat);mm=0
        for i in range(n):
            m = len(mat[i])
            mm = max(mm,m)
            for j in range(m):
                g[i+j].append(mat[i][j])
        ans = []
        for i in range(mm+n-1):
                ans+= g[i][::-1]
        return ans