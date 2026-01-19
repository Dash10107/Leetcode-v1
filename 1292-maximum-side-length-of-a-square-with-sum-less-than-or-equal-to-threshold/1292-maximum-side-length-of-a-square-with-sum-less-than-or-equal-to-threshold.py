class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n=len(mat);m=len(mat[0])
        row = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                row[i+1][j+1]=row[i][j+1]+row[i+1][j]-row[i][j]+mat[i][j]
        
        def check(k):
            for i in range(n-k+1):
                for j in range(m-k+1):
                    total = (row[i+k][j+k]-row[i][j+k]-row[i+k][j]+row[i][j])
                    if total<=threshold:
                        return True
            return False
        lo,hi,ans = 1,min(n,m),0
        while lo<=hi:
            mid = (lo+hi)//2
            if check(mid):
                ans = mid
                lo = mid+1
            else:
                hi=mid-1
        return ans