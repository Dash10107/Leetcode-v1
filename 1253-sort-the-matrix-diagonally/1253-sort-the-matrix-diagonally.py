class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        n=len(mat);m=len(mat[0])
        for i in range(n):
            for j in range(m):
                g[i-j].append(mat[i][j])
        for key in g:
            g[key].sort(reverse=True)
        for i in range(n):
            for j in range(m):
                mat[i][j]= g[i-j].pop()
        return mat