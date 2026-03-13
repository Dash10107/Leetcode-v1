class Solution:
    def minNumberOfSeconds(self, height: int, workerTimes: List[int]) -> int:

        def can(mid):
            total = 0
            for t in workerTimes:
                l, r = 0, height
                best = 0

                while l <= r:
                    m = (l + r) // 2
                    time = t * m * (m + 1) // 2
                    if time <= mid:
                        best = m
                        l = m + 1
                    else:
                        r = m - 1

                total += best
                if total >= height:
                    return True

            return False

        low = 1
        high = min(workerTimes) * height * (height + 1) // 2

        ans = high
        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans