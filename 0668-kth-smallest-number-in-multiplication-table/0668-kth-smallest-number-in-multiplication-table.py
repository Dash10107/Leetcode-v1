class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(mid):
            c = 0 
            for i in range(1,m+1):
                add = min(mid//i,n)
                if add==0:break
                c+=add
            return c>=k
        left, right = 1, n * m
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left 