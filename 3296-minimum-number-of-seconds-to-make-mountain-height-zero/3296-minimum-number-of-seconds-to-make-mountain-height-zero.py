class Solution:
    def minNumberOfSeconds(self, height: int, workerTimes: List[int]) -> int:
        def can(mid):
            total = 0
            for t in workerTimes:
                val = (2 * mid) // t
                x = int((math.sqrt(1 + 4 * val) - 1) // 2)
                total += x
                if total >= height:
                    return True
            return False

        low = 1
        high = min(workerTimes) * height * (height + 1) // 2
        ans = high
        while low<=high:
            mid = (low+high)//2
            if can(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans