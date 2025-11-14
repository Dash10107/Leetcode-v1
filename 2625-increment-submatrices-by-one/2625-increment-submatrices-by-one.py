class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        s = [[0]*n for _ in range(n)]
        for r1,c1,r2,c2 in queries:
            for r in range(r1,r2+1):
                s[r][c1]+=1
                if c2+1<n:s[r][c2+1]-=1
        for i in range(n):
            for j in range(1,n):
                s[i][j]+=s[i][j-1]
        return s