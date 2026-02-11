class Solution:
    def twoEggDrop(self, n: int) -> int:
        left = 1;right=n
        def good(x):
            floors = 0
            while x>0:
                floors+=x
                x-=1
            return floors>=n
        while left<right:
            mid = (left+right)//2
            if good(mid):
                right = mid
            else:
                left = mid+1
        return left