class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)< m*k:
            return -1
        def can(mid):
            boq,flow=0,0
            for bloom in bloomDay:
                if bloom>mid:
                    flow=0
                else:
                    boq+=(flow+1)//k
                    flow=(flow+1)%k
            return boq>=m
        left = 1;right = max(bloomDay)
        while left<right:
            mid = left+(right-left) //2
            if can(mid):
                right = mid
            else:
                left = mid+1
        return left